#!/usr/bin/env python3
"""Render all pages of a local PDF to PNG for visual inspection."""
import argparse
import pathlib
import sys
try:
    import fitz
except ImportError:
    raise SystemExit("PyMuPDF is required: python3 -m pip install pymupdf")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--scale", type=float, default=2.0)
    args = ap.parse_args()
    out = pathlib.Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(args.pdf)
    for i, page in enumerate(doc):
        target = out / f"page-{i+1:03d}.png"
        page.get_pixmap(matrix=fitz.Matrix(args.scale, args.scale), alpha=False).save(target)
        print(target)

if __name__ == "__main__":
    main()
