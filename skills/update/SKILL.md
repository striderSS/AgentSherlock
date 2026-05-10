---
description: Re-ingest a raw source that has changed and propagate the diff into the wiki.
---

You are executing the **update** workflow for this wiki. Use this when a file under `raw/` has been modified after its initial ingest and the wiki needs to reflect the changes.

The human will provide a file path under `raw/`. If they haven't, ask for it before proceeding.

## Steps

1. **Preprocess the file.** Check the extension and apply the rule from `wiki-schema.md § File Preprocessing`. Read the current version of the raw file.

2. **Read the existing source page.** Open `wiki/sources/<slug>.md` for this source. If it doesn't exist, run the `/ingest` workflow instead.

3. **Diff the content.** Compare the current raw file against what was captured in the source page (Summary, Key Points, Notable Quotes). Identify:
   - New information added
   - Information removed or changed
   - Claims that now contradict the existing wiki

4. **Update the source page.** Revise Summary, Key Points, Notable Quotes, and My Notes to reflect the new version. Do not substantially change the slug or page structure.

5. **Read `wiki/index.md`.** Identify concept and topic pages linked from this source page.

6. **Propagate changes to concept and topic pages.** For each affected page:
   - Incorporate new information
   - Remove or qualify claims that are no longer supported
   - Flag new contradictions with other sources
   - Update the `updated` frontmatter date

7. **Update `wiki/overview.md`** if the changes shift the big picture.

8. **Update `wiki/index.md`** if any pages were added or removed.

9. **Append to `wiki/log.md`** using the format from `wiki-schema.md § log.md Format`:
   ```
   ## [YYYY-MM-DD] update | <Source Title>
   ```
   Include a brief summary of what changed.

10. **Report back.** Describe what was different in the source, which wiki pages were affected, and any new contradictions or open questions that emerged.
