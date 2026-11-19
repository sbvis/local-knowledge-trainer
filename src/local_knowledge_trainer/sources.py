"""Acquire GitHub repositories, HTTPS documents and local files without executing them.

Remote failures are reported individually. Successful downloads are stored atomically
and can be reused by later runs when a common cache directory is supplied.
"""
import hashlib
import ipaddress
import os
import re
import shutil
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path

from .common import info, run

MAX_DOWNLOAD = 20 * 1024 * 1024
USER_AGENT = "LocalKnowledgeTrainer/0.3 (local source preparation)"
DEFAULT_DOWNLOAD_TIMEOUT = 20
DEFAULT_DOWNLOAD_RETRIES = 1


@dataclass(frozen=True)
class Source:
    kind: str  # repo, url, local
    origin: str
    path: Path
    commit: str = ""


@dataclass(frozen=True)
class SourceFailure:
    origin: str
    kind: str
    reason: str

    def as_dict(self):
        return asdict(self)


def repository_coordinates(url):
    """Parse a GitHub repository homepage URL, rejecting subpaths and foreign hosts."""
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or (parsed.hostname or "").lower() != "github.com":
        return None
    parts = [part for part in parsed.path.strip("/").split("/") if part]
    if len(parts) != 2:
        return None
    owner, repo = parts[0], parts[1].removesuffix(".git")
    if not (re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}", owner)
            and re.fullmatch(r"[A-Za-z0-9_.-]+", repo)):
        return None
    return owner, repo


def classify(value):
    """Return repo, url or local. Reject non-HTTPS URL schemes."""
    if re.match(r"^[A-Za-z]:[\\/]", value):
        return "local"
    if repository_coordinates(value):
        return "repo"
    if repository_tree(value):
        return "repo"
    parsed = urllib.parse.urlparse(value)
    if parsed.scheme in {"http", "https"}:
        if parsed.scheme != "https":
            raise ValueError("Only HTTPS document URLs are supported")
        return "url"
    if parsed.scheme:
        raise ValueError(f"Unsupported URL scheme: {parsed.scheme}")
    return "local"


def repository_tree(value):
    """Parse a GitHub tree URL whose ref is one URL-encoded path component."""
    parsed = urllib.parse.urlparse(value)
    parts = parsed.path.strip('/').split('/')
    if len(parts) < 4 or parts[2] != 'tree':
        return None
    parent = urllib.parse.urlunparse((parsed.scheme, parsed.netloc, '/' + '/'.join(parts[:2]), '', '', ''))
    if not repository_coordinates(parent):
        return None
    ref = urllib.parse.unquote(parts[3])
    subpath = urllib.parse.unquote('/'.join(parts[4:]))
    if not ref or ref.startswith('-') or any(part in {'.', '..'} for part in subpath.split('/')):
        raise ValueError('Invalid GitHub tree ref or directory')
    return parent, ref, subpath


def _safe_filename(url):
    name = Path(urllib.parse.unquote(urllib.parse.urlparse(url).path)).name
    name = re.sub(r"[^A-Za-z0-9._-]", "_", name)[:90]
    return name or "document.html"


def normalize_document_url(url):
    """Support ordinary GitHub 'blob' links by turning them into raw-file links."""
    parsed = urllib.parse.urlparse(url)
    if parsed.hostname == "github.com":
        parts = parsed.path.strip("/").split("/")
        if len(parts) >= 5 and parts[2] == "blob":
            return "https://raw.githubusercontent.com/" + "/".join(parts[:2] + parts[3:])
    return url


def _public_https(url):
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname:
        return False
    host = parsed.hostname.lower()
    if host == "localhost" or host.endswith(".localhost"):
        return False
    try:
        return ipaddress.ip_address(host).is_global
    except ValueError:
        return True  # DNS may resolve privately; URL sources are user-supplied and trusted.


def _retryable(exc):
    """Retry transient network errors, not permanently missing/invalid documents."""
    if isinstance(exc, urllib.error.HTTPError):
        return exc.code in {408, 425, 429, 500, 502, 503, 504}
    return isinstance(exc, (urllib.error.URLError, TimeoutError, ConnectionError))


def get_document(url, destination, *, timeout=DEFAULT_DOWNLOAD_TIMEOUT,
                 retries=DEFAULT_DOWNLOAD_RETRIES):
    """Fetch one bounded document; write only after successful complete download.

    A failed or interrupted request never leaves a partially downloaded file
    that could be mistaken for a cached, valid document on the next run.
    """
    if timeout <= 0 or retries < 0:
        raise ValueError("Download timeout must be positive and retries nonnegative")
    normalized = normalize_document_url(url)
    if not _public_https(normalized):
        raise ValueError("Document URL must use public HTTPS")
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(normalized, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                if not _public_https(response.url):
                    raise ValueError("Redirected to a non-public HTTPS URL")
                length = response.headers.get("Content-Length")
                if length and int(length) > MAX_DOWNLOAD:
                    raise ValueError("Remote document exceeds the 20 MiB limit")
                data = response.read(MAX_DOWNLOAD + 1)
            if len(data) > MAX_DOWNLOAD:
                raise ValueError("Remote document exceeds the 20 MiB limit")
            if length and len(data) != int(length):
                raise ValueError("Remote document was truncated during download")
            if not data:
                raise ValueError("Remote document is empty")
            if destination.suffix.lower() == ".pdf" and not data.lstrip().startswith(b"%PDF-"):
                raise ValueError("Expected PDF but remote URL returned a different file")
            partial = destination.with_name(destination.name + ".part")
            try:
                partial.write_bytes(data)
                os.replace(partial, destination)
            finally:
                partial.unlink(missing_ok=True)
            return destination
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            if attempt >= retries or not _retryable(exc):
                if isinstance(exc, urllib.error.HTTPError):
                    raise RuntimeError(f"Unable to fetch {normalized}: HTTP {exc.code}") from exc
                raise RuntimeError(f"Unable to fetch {normalized}: {exc}") from exc
            info(f"Document request failed ({exc}); retrying ({attempt + 1}/{retries})")
            time.sleep(min(2 ** attempt, 4))
    raise AssertionError("Unreachable retry loop")


def _clone_repo(entry, target, *, retries, ref=None):
    for attempt in range(retries + 1):
        try:
            branch = ['--branch', ref] if ref else []
            run(["git", "clone", "--depth", "1", "--single-branch", *branch, "--", entry, target])
            return
        except subprocess.CalledProcessError:
            # git clone may leave an incomplete checkout; never treat it as cached.
            if target.is_dir() and not target.is_symlink():
                shutil.rmtree(target)
            if attempt >= retries:
                raise
            info(f"Repository clone failed; retrying ({attempt + 1}/{retries})")
            time.sleep(min(2 ** attempt, 4))


def _acquire_one(entry, root, *, timeout, retries):
    tree = repository_tree(entry)
    if tree:
        parent, ref, subpath = tree
        source = _acquire_one(parent, root, timeout=timeout, retries=retries)
        branch = subprocess.check_output(['git', '-C', str(source.path), 'branch', '--show-current'], text=True).strip()
        if branch != ref:
            slug = hashlib.sha256(entry.encode()).hexdigest()[:12]
            target = root / 'trees' / slug
            if not target.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                _clone_repo(parent, target, retries=retries, ref=ref)
            commit = subprocess.check_output(['git', '-C', str(target), 'rev-parse', '--verify', 'HEAD'], text=True).strip()
            source = Source('repo', parent, target, commit)
        directory = (source.path / subpath).resolve()
        if not directory.is_relative_to(source.path.resolve()) or not directory.is_dir():
            raise ValueError(f'GitHub tree directory is missing or outside the checkout: {subpath}')
        return Source('repo', entry, directory, source.commit)
    kind = classify(entry)
    if kind == "repo":
        owner, repo = repository_coordinates(entry)
        slug = hashlib.sha256(entry.encode()).hexdigest()[:8]
        target = root / "repos" / f"{owner}-{repo}-{slug}"
        if target.is_symlink():
            raise ValueError(f"Refusing to use a symlinked cache path: {target}")
        if target.exists():
            try:
                commit = subprocess.check_output(
                    ["git", "-C", str(target), "rev-parse", "--verify", "HEAD"],
                    text=True, stderr=subprocess.DEVNULL).strip()
                if not (target / ".git").exists():
                    raise ValueError("Checkout metadata missing")
                info(f"Using cached repository {owner}/{repo}")
                return Source("repo", entry, target, commit)
            except (subprocess.CalledProcessError, ValueError):
                info(f"Removing incomplete repository cache for {owner}/{repo}")
                if target.is_dir():
                    shutil.rmtree(target)
                else:
                    target.unlink()
        info(f"Cloning {owner}/{repo}")
        target.parent.mkdir(parents=True, exist_ok=True)
        _clone_repo(entry, target, retries=retries)
        commit = subprocess.check_output(
            ["git", "-C", str(target), "rev-parse", "--verify", "HEAD"],
            text=True, stderr=subprocess.DEVNULL).strip()
        return Source("repo", entry, target, commit)
    if kind == "url":
        slug = hashlib.sha256(entry.encode()).hexdigest()[:10]
        target = root / "documents" / f"{slug}-{_safe_filename(entry)}"
        if target.is_symlink():
            raise ValueError(f"Refusing to use a symlinked cache path: {target}")
        valid_cache = target.is_file() and target.stat().st_size > 0
        if valid_cache and target.suffix.lower() == ".pdf":
            with target.open("rb") as cached:
                valid_cache = cached.read(16).lstrip().startswith(b"%PDF-")
        if valid_cache:
            info(f"Using cached document {_safe_filename(entry)}")
        else:
            info(f"Downloading document {entry}")
            get_document(entry, target, timeout=timeout, retries=retries)
        return Source("url", entry, target)
    target = Path(entry).expanduser().resolve()
    if not target.is_file() and not target.is_dir():
        raise FileNotFoundError(f"Local source does not exist: {entry}")
    return Source("local", str(target), target)


def acquire(entries, root, *, failures=None, strict=False,
            timeout=DEFAULT_DOWNLOAD_TIMEOUT, retries=DEFAULT_DOWNLOAD_RETRIES):
    """Acquire independent sources; skip/report failures unless strict=True.

    `failures`, when provided, is populated with SourceFailure records. In
    non-strict mode at least one usable source is required; callers also need
    to verify that the usable sources yielded actual readable content.
    """
    if timeout <= 0 or retries < 0:
        raise ValueError("Download timeout must be positive and retries nonnegative")
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    sources = []
    for entry in dict.fromkeys(entries):
        try:
            sources.append(_acquire_one(entry, root, timeout=timeout, retries=retries))
        except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError,
                urllib.error.URLError) as exc:
            kind = "unknown"
            try:
                kind = classify(entry)
            except ValueError:
                pass
            failure = SourceFailure(entry, kind, str(exc))
            if failures is not None:
                failures.append(failure)
            if strict:
                raise
            print(f"  WARNING: Skipping {kind} source {entry}: {exc}", flush=True)
    if not sources:
        raise RuntimeError(f"No usable sources: all {len(list(dict.fromkeys(entries)))} source(s) failed. "
                           "See warnings above; save remote documents locally or check URLs.")
    return sources
