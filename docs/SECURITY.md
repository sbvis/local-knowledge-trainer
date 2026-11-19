# Security, privacy and licenses

- **Local-only runtime:** Running the exported model and SQLite database requires no API, subscription, browser or server. During building, selected Git/HTTPS URLs and pretrained weights are downloaded, and Python/C++ dependencies may be fetched from package registries.
- **Source trust:** Source files can contain malicious prompt instructions, misleading documentation and secrets. The retrieval prompt marks excerpts as untrusted data. Never execute cloned repositories, and never promote retrieved text to system instructions.
- **Privacy:** Do not upload private sources, model artifacts or training logs publicly. Fine-tuned weights and SQLite records may encode sensitive information from the input data.
- **Licensing:** The repository code is MIT-licensed. Input GitHub projects, documents and pretrained models have independent usage/redistribution conditions.
- **Credential handling:** Use ordinary Git authentication for authorized private repositories. Do not put personal access tokens in repository URLs or committed `.env` files. The `.gitignore` excludes common secrets and training outputs by default.
- **Source handling:** File/byte caps mitigate accidental resource exhaustion. The HTTPS downloader restricts schemes and size, but DNS rebinding/internal network protection is not a hardened security boundary: only supply trusted URLs in trusted environments.
- **Release integrity:** Verify `SHA256SUMS.txt` before transporting or distributing weights. Optional GGUF shards must remain complete, co-located and unmodified.
- **Evaluation:** Local generated answers can still be wrong. Evaluate abstentions, citations, prompt injection resistance and data leakage using independent, human-reviewed examples.
