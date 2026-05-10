---
description: Health-check the wiki for contradictions, orphans, stale content, and missing pages.
---

You are executing the **lint** workflow for this wiki.

## Steps

1. **Read every page in `wiki/`.** Start with `index.md`, then read all sources, concepts, topics, and queries.

2. **Check for the following issues:**

   | Severity | Issue type | Description |
   |----------|-----------|-------------|
   | High | Contradiction | Same claim stated differently or oppositely across two pages |
   | High | Stale synthesis | A concept or topic page whose synthesis predates newer sources that changed the picture |
   | Medium | Orphan page | A page with no inbound links from index or other pages |
   | Medium | Missing page | A concept referenced in multiple places but lacking its own dedicated page |
   | Low | Missing cross-reference | Two clearly related pages that don't link to each other |
   | Low | Data gap | A claim that could be strengthened or checked with a targeted search or new source |

3. **Fix what you can autonomously:**
   - Add missing cross-references
   - Create stub pages for missing concepts (mark them with a `stub: true` frontmatter flag)
   - Update `wiki/index.md` for any orphan or missing-page fixes

4. **Flag what needs human input:**
   - Contradictions (ask the human which version is correct)
   - Stale synthesis that requires re-reading a source to resolve
   - Data gaps that would benefit from a new source

5. **Report findings** grouped by severity: High → Medium → Low. For each issue, state the affected page(s), the problem, and what was done or what you need from the human.

6. **Append to `wiki/log.md`** using the format from `wiki-schema.md § log.md Format`:
   ```
   ## [YYYY-MM-DD] lint | Health check
   ```
   Include issue counts and a brief summary of what was fixed vs. still open.
