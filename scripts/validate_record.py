#!/usr/bin/env python3
"""Report deterministic model-vs-attachment naming conflicts in a fetched Feishu record."""
import argparse
import json
import pathlib
import re

MODEL_RE = re.compile(r"(?P<pins>\d+)P(?P<height>\d{3})", re.I)

def variants(value):
    if not isinstance(value, list):
        return []
    return [(x.get("name") or "") for x in value if isinstance(x, dict)]

def parse_variant(text):
    m = MODEL_RE.search(text or "")
    return (int(m.group("pins")), int(m.group("height"))) if m else None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("record")
    args = ap.parse_args()
    record = json.loads(pathlib.Path(args.record).read_text(encoding="utf-8"))
    model = record.get("内部型号") or ""
    expected = parse_variant(model)
    issues = []
    if not expected:
        issues.append(f"无法从内部型号解析 P 数和高度代码：{model!r}")
    for name in variants(record.get("3D图")):
        found = parse_variant(name)
        if expected and found and found != expected:
            issues.append(f"3D 附件变体不匹配：内部型号 {model}，附件 {name}")
    title = record.get("中文产品名称") or ""
    title_pin_counts = [int(value) for value in re.findall(r"(?:^|[-_\s])(\d+)P(?:[-_\s]|$)", title, re.I)]
    if expected and title_pin_counts and expected[0] not in title_pin_counts:
        issues.append(f"中文产品名称 P 数与内部型号不一致：{title}")
    height = record.get("塑胶高度(mm)")
    if expected and height:
        try:
            if round(float(height) * 100) != expected[1]:
                issues.append(f"塑胶高度字段与内部型号高度代码不一致：{height} vs {expected[1]}")
        except ValueError:
            issues.append(f"塑胶高度无法解析：{height!r}")
    report = {"record_id": record.get("record_id"), "model": model, "expected_variant": expected,
              "issues": issues, "status": "needs_review" if issues else "filename_checks_passed",
              "note": "仍需人工/视觉核对预览图和2D图纸中的实际针数与结构。"}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(1 if issues else 0)

if __name__ == "__main__":
    main()
