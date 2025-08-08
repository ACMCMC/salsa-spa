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
    # Test one sample per category
    # Collect results for JSON report
    import json
    import logging
    report = []

    for lvl in CEFR_LEVELS:
        sample = next((row for row in ds if row["category"] == lvl), None)
        assert sample is not None, f"No sample for category {lvl}"
        text = sample["text"]
        result, _ = grade_with_probabilities(text=text)
        logging.info(
            f"Level: {lvl}, Grade: {result['grade']:.2f}, Probabilities: {result['probabilities']}"
        )
        assert 0.0 <= result["grade"] <= 1.0
        assert abs(sum(result["probabilities"].values()) - 1.0) < 1e-6
        # Store result for report
        report.append({
            "level": lvl,
            "grade": result["grade"],
            "probabilities": result["probabilities"]
        })

    # Save report to JSON file
    with open("outputs/cefr_test_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    logging.info("Saved CEFR test report to outputs/cefr_test_report.json")
