"""
Experimental pipeline: test salsa-spa grading on concatenated Hugging Face datasets.
"""

import pytest
from datasets import load_dataset
from salsa_spa.grader_prob import grade_with_probabilities
from datasets import concatenate_datasets

CEFR_LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]


def test_concat_cefr_datasets():
    # Load hablacultura
    ds1 = load_dataset("lmvasque/hablacultura", split="train")
    # Load readability-es
    ds2 = load_dataset(
        "somosnlp-hackathon-2022/readability-es-hackathon-pln-public", split="train"
    )
    # Filter to only CEFR categories
    ds1 = ds1.filter(lambda x: x["category"] in CEFR_LEVELS)
    ds2 = ds2.filter(lambda x: x["category"] in CEFR_LEVELS)

    # Remove columns other than 'text' and 'category'
    ds1 = ds1.remove_columns(
        [col for col in ds1.column_names if col not in ["text", "category"]]
    )
    ds2 = ds2.remove_columns(
        [col for col in ds2.column_names if col not in ["text", "category"]]
    )

    # Concatenate datasets
    ds = concatenate_datasets([ds1, ds2])
    assert len(ds) > 0, "No data after filtering!"
    # Take 100 samples per CEFR level, compute averages, and report
    import json
    import logging
    report = []
    summary = {}

    for lvl in CEFR_LEVELS:
        # Get up to 100 samples for this level
        samples = [row for row in ds if row["category"] == lvl][:100]
        grades = []
        probs_list = []
        for sample in samples:
            text = sample["text"]
            result, _ = grade_with_probabilities(text=text)
            grades.append(result["grade"])
            probs_list.append(result["probabilities"])
            report.append({
                "level": lvl,
                "grade": result["grade"],
                "probabilities": result["probabilities"]
            })
        if grades:
            # Average grade
            avg_grade = sum(grades) / len(grades)
            # Average probabilities per class
            avg_probs = {}
            for key in probs_list[0].keys():
                avg_probs[key] = sum(p[key] for p in probs_list) / len(probs_list)
            summary[lvl] = {
                "avg_grade": avg_grade,
                "avg_probabilities": avg_probs,
                "n_samples": len(grades)
            }
            logging.info(
                f"Level: {lvl}, Avg Grade: {avg_grade:.2f}, Avg Probabilities: {avg_probs}"
            )
        else:
            summary[lvl] = {
                "error": f"No samples for category {lvl}"
            }

    # Save report and summary to JSON file before assertions
    with open("outputs/cefr_test_report.json", "w", encoding="utf-8") as f:
        json.dump({"samples": report, "summary": summary}, f, ensure_ascii=False, indent=2)
    logging.info("Saved CEFR test report to outputs/cefr_test_report.json")

    # Now do assertions
    for lvl in CEFR_LEVELS:
        entry = summary[lvl]
        if "error" in entry:
            assert False, entry["error"]
        avg_grade = entry["avg_grade"]
        avg_probs = entry["avg_probabilities"]
        assert 0.0 <= avg_grade <= 1.0
        assert abs(sum(avg_probs.values()) - 1.0) < 1e-6
