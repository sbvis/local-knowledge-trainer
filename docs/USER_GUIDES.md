# Writing reliable user-interface guides

The project is general-purpose: any application can provide version-specific
user tutorials. Do **not** infer UI click sequences from function names alone.

## Include this information

1. **Application and version/build** covered by the instructions.
2. **User objective:** what the action achieves, in nontechnical language.
3. **Entry point:** verified names of the window, menu, panel or toolbar.
4. **Sequence:** real clicks, controls, fields, values and expected outcome.
5. **Exceptions:** prerequisites, unavailable controls, alternate workflows.
6. **Evidence:** official manuals, screenshots, release notes, or a user-verified
   walkthrough. Distinguish tested instructions from guesses.

### Sample document structure (fill with facts about your own software)

```markdown
# Application name — User guide for version X.Y

## Adjust a display parameter

Prerequisite: [required dataset or view]

1. [Verified navigation to the correct view]
2. [Verified menu, panel or setting name]
3. [Verified adjustment and confirmation]

Expected result: [what users should see]

Source: [official document or date tested]
```

These bracketed fields are *authoring prompts*, not steps to ship as model
knowledge. Replace each with a checked fact before indexing the guide.

## Adding a guide to an existing offline release

```sh
./start.command add-guide runs/RELEASE_ID/release ./verified-ui-guide.md \
  --source https://github.com/example/project
```

The file content is copied into `knowledge.db` as chunks identified by the
source URL. No model retraining takes place. Rerunning the command with the
same source URL and filename replaces the guide's previous chunks.

## Evaluate separately

- **General:** Can the model explain unfamiliar concepts accurately?
- **Developer:** Can it name real code symbols, files and limitations?
- **End user:** Does it give exact steps supported by the correct software
  version's documentation, without presenting code changes?
- **Missing evidence:** Does it decline to invent unverified UI controls?

Save at least 20 independent, checked evaluation questions per intended user
audience. The generated training-loss values and retrieval hit rates do not
measure end-user task success.
