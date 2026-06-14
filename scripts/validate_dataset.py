from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    records = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/final/tcode_v4_2700.jsonl")
    parser.add_argument("--out", default="results/dataset_validation_summary.json")
    args = parser.parse_args()

    records = read_jsonl(Path(args.input))
    errors = []
    ids = []
    raws = []

    for i, r in enumerate(records):
        rec_id = r.get("id")
        ids.append(rec_id)
        raws.append(r.get("raw_command"))

        tokens = r.get("tokens", [])
        boundary = r.get("boundary_labels", [])
        task = r.get("task_token_labels", [])

        if len(tokens) != len(boundary):
            errors.append({"id": rec_id, "error": "tokens_boundary_length_mismatch"})
        if len(tokens) != len(task):
            errors.append({"id": rec_id, "error": "tokens_task_length_mismatch"})

    summary = {
        "record_count": len(records),
        "domain_distribution": Counter([r.get("domain", "unknown") for r in records]),
        "task_count_distribution": Counter([str(r.get("task_count", "unknown")) for r in records]),
        "duplicate_id_count": sum(1 for _, c in Counter(ids).items() if c > 1),
        "duplicate_raw_command_count": sum(1 for _, c in Counter(raws).items() if c > 1),
        "error_count": len(errors),
        "errors_preview": errors[:50],
    }

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
