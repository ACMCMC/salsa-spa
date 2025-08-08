"""
Grading and probability calculation for CEFR levels.
"""

from collections import Counter
import math
from .word_level import detect_word_levels
from .vocab_lists import level_dict


def grade_with_probabilities(text: str) -> tuple[dict, dict]:
    # Get word-level CEFR assignments
    word_levels = detect_word_levels(text=text, level_dictionary=level_dict)
    levels = [level for _, level in word_levels]
    total_words = len(levels)
    unique_words = len(set([w for w, _ in word_levels]))
    unknown_words = sum(1 for l in levels if l == "A0" or l == "No results")
    input_length = len(text)

    # All possible levels
    all_levels = ["A0", "A1", "A2", "B1", "B2", "C1", "C2"]
    level_values = {"A0": 0, "A1": 1, "A2": 2, "B1": 3, "B2": 4, "C1": 5, "C2": 6}
    levels = [l if l in all_levels else "A0" for l in levels]
    freq = Counter(levels)
    probabilities = {
        lvl: freq.get(lvl, 0) / total_words if total_words else 0.0
        for lvl in all_levels
    }
    exp_weights = {lvl: math.exp(level_values[lvl]) for lvl in all_levels}
    # Only use present levels for normalization
    present_levels = [
        lvl for lvl in all_levels if probabilities[lvl] > 0 and lvl != "A0"
    ]
    numerator = sum(probabilities[lvl] * exp_weights[lvl] for lvl in present_levels)
    denominator = sum(exp_weights[lvl] for lvl in present_levels)
    grade = (
        numerator / denominator if denominator and probabilities["A0"] < 1.0 else 0.0
    )
    # Main output dict
    result = {
        "grade": grade,
        "probabilities": probabilities,
        "stats": {
            "total_words": total_words,
            "unique_words": unique_words,
            "unknown_words": unknown_words,
            "input_length": input_length,
        },
    }
    # Word-level output dict (not used for now)
    word_level_dict = {w: l for w, l in word_levels}
    return result, word_level_dict
