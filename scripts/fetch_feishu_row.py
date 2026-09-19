#!/usr/bin/env python3
"""Resolve a Feishu Base URL, fetch one visible view row, and download its attachments."""
import argparse
import json
import pathlib
import subprocess
import sys

FIELDS = [
    "Series ID", "中文产品名称", "英文产品名称", "内部型号", "预览图", "2D图纸",
    "3D图", "替换图纸", "实物原图", "塑胶高度(mm)", "间距mm", "备注"
]

def run(cmd):
    p = subprocess.run(cmd, text=True, capture_output=True)
    if p.returncode:
        sys.stderr.write(p.stderr or p.stdout)
        raise SystemExit(p.returncode)
    return p.stdout

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--row", required=True, type=int, help="1-based visible row number in the URL view")
    ap.add_argument("--out-dir", required=True)
    args = ap.parse_args()
    if args.row < 1:
        ap.error("--row must be >= 1")

    out = pathlib.Path(args.out_dir).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    resolved = json.loads(run(["lark-cli", "base", "+url-resolve", "--url", args.url, "--as", "user"]))
    data = resolved.get("data", {})
    base, table, view = data.get("base_token"), data.get("table_id"), data.get("view_id")
    if not (base and table and view):
        raise SystemExit("URL must resolve to a Base table view with base_token, table_id and view_id")

    ndjson = out / "record.ndjson"
    cmd = ["lark-cli", "base", "+record-list", "--base-token", base, "--table-id", table,
           "--view-id", view, "--offset", str(args.row - 1), "--limit", "1",
           "--format", "ndjson", "--output", str(ndjson), "--as", "user"]
    for field in FIELDS:
        cmd += ["--field-id", field]
    summary = json.loads(run(cmd))
    rows = [json.loads(line) for line in ndjson.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(rows) != 1:
        raise SystemExit(f"Expected one record at visible row {args.row}, got {len(rows)}")
    record = rows[0]
    record["_source"] = {"url": args.url, "visible_row": args.row, "base_token": base, "table_id": table, "view_id": view, "rev": summary.get("rev")}
    (out / "record.json").write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")

    attachments = out / "attachments"
    attachments.mkdir(exist_ok=True)
    run(["lark-cli", "base", "+record-download-attachment", "--base-token", base,
         "--table-id", table, "--record-id", record["record_id"], "--output", str(attachments), "--as", "user"])
    print(json.dumps({"ok": True, "visible_row": args.row, "record_id": record["record_id"],
                      "model": record.get("内部型号"), "record": str(out / "record.json"),
                      "attachments": str(attachments)}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
