#!/usr/bin/env python3
"""Convert raw source files to plain text and print to stdout."""

import os
import sys


def convert_rtf(path: str) -> str:
    from striprtf.striprtf import rtf_to_text
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return rtf_to_text(f.read())


def convert_docx(path: str) -> str:
    from docx import Document
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)


CONVERTERS = {
    ".rtf": convert_rtf,
    ".docx": convert_docx,
}


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 tools/preprocess.py <file>", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)

    ext = os.path.splitext(path)[1].lower()
    converter = CONVERTERS.get(ext)
    if converter is None:
        print(f"Unsupported format: {ext}. Supported: {', '.join(CONVERTERS)}", file=sys.stderr)
        sys.exit(1)

    print(converter(path))


if __name__ == "__main__":
    main()
