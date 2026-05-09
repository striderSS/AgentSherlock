# AgentSherlock

A personal knowledge wiki maintained by LLMs. Raw sources go in; structured, interlinked markdown pages come out. The LLM does the bookkeeping — summarizing, cross-referencing, filing, flagging contradictions. You curate sources and ask questions.

## How it works

Drop a source into `raw/`, tell your LLM to ingest it, and it will create a summary page, update related concept and topic pages, and keep the index current. Ask a question and the LLM reads the wiki to synthesize an answer — optionally filing the result as a new page. Periodically ask it to lint the wiki for contradictions, orphans, and gaps.

## Directory Structure

```
.
├── wiki-schema.md       # Wiki structure, page formats, and LLM workflows
├── CLAUDE.md            # Claude Code entry point — references wiki-schema.md
├── AGENTS.md            # OpenAI Codex entry point — references wiki-schema.md
│
├── raw/                 # Your source documents — immutable, never modified by the LLM
│   └── assets/          # Images and attachments referenced by sources
│
└── wiki/                # LLM-maintained knowledge base
    ├── index.md         # Master catalog of all pages — updated on every ingest
    ├── log.md           # Append-only activity log (ingest / query / lint entries)
    ├── overview.md      # High-level synthesis of the entire wiki
    ├── sources/         # One page per raw source
    ├── concepts/        # Recurring ideas, frameworks, mental models
    ├── topics/          # Broad subject areas that aggregate concepts and sources
    └── queries/         # Valuable Q&A sessions worth preserving
```

> **Note:** `raw/` contents and `wiki/**/*.md` are excluded from version control (see `.gitignore`). Only the scaffold and schema are tracked — wiki content stays local.

## Key Files

### `wiki-schema.md`

The core of the project. Defines everything the LLM needs to maintain the wiki:

- **Directory layout** — where each page type lives and why
- **Page formats** — frontmatter fields and section structure for each of the four page types (source, concept, topic, query)
- **Naming conventions** — slug format, title casing, wiki link syntax
- **`index.md` and `log.md` formats** — so both files stay consistent and grep-parseable
- **Three workflows:**
  - *Ingest* — 10-step process from reading a raw source to updating the index and log
  - *Query* — read the index, drill into relevant pages, synthesize an answer, optionally file it
  - *Lint* — health-check for contradictions, orphan pages, missing cross-references, data gaps

This file is LLM-agnostic. It can be pasted as a system prompt for any LLM, or loaded automatically via the per-LLM wrapper files below.

### `CLAUDE.md`

Single-line entry point for [Claude Code](https://claude.ai/code). Claude Code automatically reads this file at the start of every session. It instructs Claude to read `wiki-schema.md` and follow it exactly — no schema content is duplicated here.

### `AGENTS.md`

Single-line entry point for OpenAI Codex (and compatible agents). Serves the same role as `CLAUDE.md` for the OpenAI toolchain.

If you use a different LLM or interface, paste the contents of `wiki-schema.md` directly into your system prompt.
