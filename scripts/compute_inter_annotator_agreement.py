from __future__ import annotations

import argparse
import ast
import csv
import json
from collections import Counter
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def parse_labels(value: str) -> list[str]:
    value = (value or "").strip()
    if not value:
        return []

    for parser in (json.loads, ast.literal_eval):
        try:
            parsed = parser(value)
            if isinstance(parsed, list):
                return [str(x).strip() for x in parsed]
        except Exception:
            pass

    if "|" in value:
        return [x.strip() for x in value.split("|") if x.strip()]
    if "," in value:
        return [x.strip() for x in value.split(",") if x.strip()]
    return [x.strip() for x in value.split() if x.strip()]


def cohen_kappa(gold: list[str], pred: list[str]) -> dict:
    if len(gold) != len(pred):
        raise ValueError(f"Length mismatch: gold={len(gold)}, pred={len(pred)}")

    n = len(gold)
    correct = sum(1 for g, p in zip(gold, pred) if g == p)
    po = correct / n if n else 0

    gold_counts = Counter(gold)
    pred_counts = Counter(pred)
    labels = set(gold_counts) | set(pred_counts)

    pe = sum((gold_counts[l] / n) * (pred_counts[l] / n) for l in labels) if n else 0
    kappa = 1.0 if pe == 1 and po == 1 else ((po - pe) / (1 - pe) if pe != 1 else 0.0)

    return {
        "n": n,
        "accuracy": po,
        "observed_agreement": po,
        "expected_agreement": pe,
        "cohen_kappa": kappa,
    }


def top_confusions(gold: list[str], pred: list[str], top_n: int = 30) -> list[dict]:
    c = Counter()
    for g, p in zip(gold, pred):
        if g != p:
            c[(g, p)] += 1

    return [{"gold": g, "annotator": p, "count": n} for (g, p), n in c.most_common(top_n)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gold-jsonl", default="data/second_annotator/second_annotator_sample_300_gold.jsonl")
    parser.add_argument("--annotator-csv", default="data/second_annotator/second_annotator_completed_anonymized.csv")
    parser.add_argument("--out-json", default="results/inter_annotator_agreement.json")
    args = parser.parse_args()

    gold_records = read_jsonl(Path(args.gold_jsonl))
    gold_by_id = {str(r.get("id")): r for r in gold_records}

    flat_gold_boundary = []
    flat_ann_boundary = []
    flat_gold_task = []
    flat_ann_task = []
    row_errors = []

    with Path(args.annotator_csv).open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rec_id = str(row.get("id", "")).strip()
            if rec_id not in gold_by_id:
                row_errors.append({"id": rec_id, "error": "id_not_found"})
                continue

            gold = gold_by_id[rec_id]
            gb = gold.get("boundary_labels", [])
            gt = gold.get("task_token_labels", [])

            ab = parse_labels(row.get("annotator_boundary_labels", ""))
            at = parse_labels(row.get("annotator_task_token_labels", ""))

            if len(gb) != len(ab):
                row_errors.append({"id": rec_id, "error": "boundary_length_mismatch", "gold": len(gb), "annotator": len(ab)})
                continue

            if len(gt) != len(at):
                row_errors.append({"id": rec_id, "error": "task_token_length_mismatch", "gold": len(gt), "annotator": len(at)})
                continue

            flat_gold_boundary.extend(gb)
            flat_ann_boundary.extend(ab)
            flat_gold_task.extend(gt)
            flat_ann_task.extend(at)

    result = {
        "boundary_labels": cohen_kappa(flat_gold_boundary, flat_ann_boundary),
        "task_token_labels": cohen_kappa(flat_gold_task, flat_ann_task),
        "boundary_top_confusions": top_confusions(flat_gold_boundary, flat_ann_boundary, 20),
        "task_token_top_confusions": top_confusions(flat_gold_task, flat_ann_task, 20),
        "row_errors": row_errors,
    }

    Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_json).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
