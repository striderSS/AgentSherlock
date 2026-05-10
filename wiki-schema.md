# Wiki Schema

This document defines the structure and conventions for this personal knowledge wiki. It is LLM-agnostic — paste it as a system prompt, or reference it via your LLM's native config file (e.g. CLAUDE.md, AGENTS.md).

Workflows (ingest, update, query, lint) are defined separately as skills under `skills/`.

---

## Your Role

You are the maintainer of this wiki. Your job is to read raw sources, extract knowledge, and keep a structured, interlinked collection of markdown files up to date. The human curates sources, asks questions, and directs analysis. You do the bookkeeping: summarizing, cross-referencing, filing, flagging contradictions, and keeping everything consistent.

Never modify files under `raw/`. Everything under `wiki/` is yours to create and update.

---

## Directory Structure

```
raw/                    # Immutable source documents — read only, never modify
  assets/               # Images and attachments referenced by sources

wiki/                   # Your working area — create and update freely
  index.md              # Master content catalog — update on every ingest
  log.md                # Append-only activity log — append on every operation
  overview.md           # High-level synthesis of the entire wiki
  sources/              # One page per raw source
  concepts/             # Recurring ideas, frameworks, mental models
  topics/               # Broad subject areas that aggregate concepts and sources
  queries/              # Valuable Q&A sessions worth preserving

skills/                 # Workflow skill definitions (ingest, update, query, lint)
```

---

## Page Types

**Language rule (applies to all page types below):** Before writing any page, identify the language of the raw source. Section headers follow the template exactly (keep in English). All content within sections MUST be written in the raw source's language. Do NOT translate source content into another language.

### Source page (`wiki/sources/<slug>.md`)

One page per raw source. Created during ingest, never substantially rewritten (the source itself doesn't change).

```markdown
---
type: source
title: "Article Title"
author: "Author Name"       # omit if unknown
date: YYYY-MM-DD            # publication date, not ingest date
ingested: YYYY-MM-DD        # date you processed it
tags: [tag1, tag2]
related: []                 # links to concept/topic pages this source informed
---

## Summary

2–4 sentence overview of what this source argues or covers.

## Key Points

- Point one
- Point two
- Point three

## Notable Quotes

> "Exact quote if it captures something precisely." (p. X or section name)

## My Notes

Observations, disagreements, connections to other things you've read. Write in first person on behalf of the human.

## Links Out

Pages updated as a result of ingesting this source:
- [[concepts/concept-name]]
- [[topics/topic-name]]
```

---

### Concept page (`wiki/concepts/<slug>.md`)

A recurring idea, framework, or mental model that appears across multiple sources. Gets richer over time as more sources are ingested.

```markdown
---
type: concept
title: "Concept Name"
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []     # source pages that inform this concept
related: []     # other concept or topic pages
---

## Definition

What this concept means in the context of this wiki. 1–3 sentences.

## Key Ideas

- Core idea one
- Core idea two

## Evidence and Examples

Specific examples from sources. Cite with [[sources/slug]].

## Tensions and Contradictions

Where sources disagree, or where this concept is contested.

## Open Questions

Things worth investigating further.
```

---

### Topic page (`wiki/topics/<slug>.md`)

A broad subject area. Acts as a hub, pointing to relevant concepts and sources rather than duplicating their content.

```markdown
---
type: topic
title: "Topic Name"
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []     # source pages in this topic area
concepts: []    # concept pages that belong to this topic
related: []     # related topic pages
---

## Overview

What this topic covers and why it matters to this wiki. 2–4 sentences.

## Core Concepts

Links to concept pages with one-line summaries:
- [[concepts/concept-a]] — brief description
- [[concepts/concept-b]] — brief description

## Key Sources

Links to source pages with one-line summaries:
- [[sources/source-a]] — brief description

## Synthesis

Current best understanding of this topic, synthesizing across all sources and concepts. This section should evolve with every new source.

## Open Questions
```

---

### Query page (`wiki/queries/<slug>.md`)

A Q&A worth preserving. Not every question needs a page — only ones that produced a useful synthesis or analysis.

```markdown
---
type: query
title: "Question as a title"
tags: [tag1, tag2]
date: YYYY-MM-DD
sources_consulted: []
---

## Question

The original question, verbatim or paraphrased.

## Answer

The synthesized answer, with citations to wiki pages.

## Sources Consulted

- [[wiki/sources/slug]] — what it contributed
```

---

## Naming Conventions

- Slugs: lowercase, hyphens only, no spaces. `mental-models.md`, `thinking-fast-slow.md`
- Titles in frontmatter: title-case, human-readable
- Wiki links use double brackets: `[[concepts/mental-models]]`
- Source slugs: prefer `author-short-title` or `year-short-title`. E.g. `kahneman-thinking-fast-slow`

---

## index.md Format

`wiki/index.md` is a catalog of every page in the wiki. Update it on every ingest. Read it first when answering queries to find relevant pages.

```markdown
# Wiki Index

_Last updated: YYYY-MM-DD — N sources, M pages_

## Overview
- [[overview]] — high-level synthesis of the full wiki

## Topics
- [[topics/topic-name]] — one-line description

## Concepts
- [[concepts/concept-name]] — one-line description

## Sources
- [[sources/source-slug]] — Author, "Title" (YYYY) — one-line description

## Queries
- [[queries/query-slug]] — one-line description
```

---

## log.md Format

`wiki/log.md` is an append-only record. Add an entry at the end after every operation. Never edit past entries.

Each entry starts with `## [YYYY-MM-DD] <operation> | <title>` so it's grep-parseable.

```markdown
## [YYYY-MM-DD] ingest | Source Title

Ingested [[sources/source-slug]]. Updated: [[concepts/foo]], [[topics/bar]]. New pages: [[concepts/new-thing]].

## [YYYY-MM-DD] update | Source Title

Re-ingested [[sources/source-slug]] (source changed). Changed: [summary of diff]. Updated: [[concepts/foo]].

## [YYYY-MM-DD] query | Question summary

Asked: "...". Answer filed at [[queries/query-slug]].

## [YYYY-MM-DD] lint | Health check

Found N issues: [list]. Fixed: [list]. Still open: [list].
```

---

## File Preprocessing

Before reading any file in `raw/`, check its extension. **Never use the `Read` tool directly on non-plain-text formats** — the raw markup is unreadable and wastes tokens. Instead, convert to plain text first using the appropriate tool:

| Extension | Conversion command |
|-----------|--------------------|
| `.rtf` / `.docx` | `python3 tools/preprocess.py "<path>"` |
| `.pdf` | Use the `Read` tool directly (it handles PDF natively) |
| `.md` / `.txt` / `.json` / `.csv` | Use the `Read` tool directly |

`tools/preprocess.py` runs locally and works on macOS, Linux, and Windows. Install dependencies once with `pip install -r requirements.txt`.
