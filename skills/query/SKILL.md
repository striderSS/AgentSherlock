---
description: Answer a question by synthesizing across wiki pages. Use when the human asks a question about content in the wiki.
---

You are executing the **query** workflow for this wiki.

The human will provide a question. If they haven't, ask for it before proceeding.

## Steps

1. **Read `wiki/index.md`.** Identify pages that are likely relevant to the question.

2. **Read those pages in full.** Drill into concept, topic, and source pages as needed.

3. **Synthesize an answer.** Write a clear answer with citations using `[[page]]` references. The answer should reflect the wiki's current state — note any open questions or gaps where the wiki doesn't yet have coverage.

4. **Ask whether to file it.** Ask the human: "Worth saving this as a query page?" If yes, proceed to step 5. If no, stop here.

5. **Create a query page.** Write `wiki/queries/<slug>.md` using the query page format from `wiki-schema.md § Page Types`. Choose a slug that captures the question concisely.

6. **Update `wiki/index.md`.** Add the new query page to the Queries section.

7. **Append to `wiki/log.md`** using the format from `wiki-schema.md § log.md Format`:
   ```
   ## [YYYY-MM-DD] query | <Question summary>
   ```
