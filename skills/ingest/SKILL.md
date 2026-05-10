---
description: Ingest a new source file into the wiki. Use when the human adds a file to raw/ and asks you to process it.
---

You are executing the **ingest** workflow for this wiki. Follow these steps exactly.

The human will provide a file path under `raw/`. If they haven't, ask for it before proceeding.

## Steps

1. **Preprocess the file.** Check the extension and apply the rule from `wiki-schema.md § File Preprocessing`. Never call `Read` directly on `.rtf` or `.docx`. Note the source language — all wiki content you write must be in that language.

2. **Summarize and confirm.** Briefly summarize the key ideas (3–5 bullet points) and ask the human if there's anything specific to focus on. Skip this step if the human asked for a batch ingest without discussion.

3. **Create the source page.** Write `wiki/sources/<slug>.md` using the source page format from `wiki-schema.md § Page Types`. Choose a slug following `wiki-schema.md § Naming Conventions`.

4. **Read `wiki/index.md`.** Identify existing concept and topic pages that this source is relevant to.

5. **Update existing pages.** For each relevant concept or topic page: add the new source reference, strengthen or challenge the existing synthesis, flag any contradictions with prior sources. Update the `updated` frontmatter date.

6. **Create new pages if needed.** If significant new ideas aren't covered anywhere, create new concept or topic pages using the formats in `wiki-schema.md § Page Types`.

7. **Update `wiki/overview.md`** if the new source meaningfully shifts the big picture.

8. **Update `wiki/index.md`.** Add the new source page and any new concept/topic pages. Increment the source and page counts.

9. **Append to `wiki/log.md`** using the format from `wiki-schema.md § log.md Format`:
   ```
   ## [YYYY-MM-DD] ingest | <Source Title>
   ```

10. **Report back.** List which pages were created, which were updated, and anything surprising or worth discussing.
