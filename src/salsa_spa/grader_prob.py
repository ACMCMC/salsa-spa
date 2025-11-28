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
    
    # Separate known and unknown words
    known_levels = ["A1", "A2", "B1", "B2", "C1", "C2"]
    known_words_count = sum(freq.get(lvl, 0) for lvl in known_levels)
    unknown_words_count = freq.get("A0", 0)
    
    # Calculate probabilities based only on known words (A1-C2)
    # This reduces the influence of A0 on the grade
    if known_words_count > 0:
        probabilities_known = {
            lvl: freq.get(lvl, 0) / known_words_count
            for lvl in known_levels
        }
    else:
        probabilities_known = {lvl: 0.0 for lvl in known_levels}
    
    # Calculate probabilities including A0 for reporting purposes
    probabilities = {
        lvl: freq.get(lvl, 0) / total_words if total_words else 0.0
        for lvl in all_levels
    }
    
    # Use more aggressive weighting for higher levels (tail of distribution)
    # Polynomial weighting gives more weight to advanced levels without being excessive
    # Using level^2 gives moderate tail weighting: C2 gets 36x weight vs A1's 1x
    poly_weights = {lvl: (level_values[lvl] ** 2) for lvl in known_levels}
    
    # Calculate grade based only on known words, with heavy tail weighting
    present_levels = [
        lvl for lvl in known_levels if probabilities_known[lvl] > 0
    ]
    
    if present_levels:
        # Calculate weighted average of level values, favoring higher levels
        # Weight both the probability and the level value
        numerator = sum(
            probabilities_known[lvl] * level_values[lvl] * poly_weights[lvl]
            for lvl in present_levels
        )
        denominator = sum(
            probabilities_known[lvl] * poly_weights[lvl] for lvl in present_levels
        )
        
        if denominator > 0:
            weighted_level_value = numerator / denominator
            # Normalize to 0-1 scale (A1=1 to C2=6, so divide by 6)
            # Cap at 1.0
            grade = min(weighted_level_value / 6.0, 1.0)
        else:
            grade = 0.0
    else:
        # Very few or no known words - assign A0
        # Threshold: if less than 10% of words are known, assign A0
        if known_words_count == 0 or (known_words_count / total_words) < 0.1:
            grade = 0.0  # A0
        else:
            # Should not reach here, but fallback
            grade = 0.0
    # Word-level output dict
    word_level_dict = {w: l for w, l in word_levels}
    
    # Group found expressions by level (excluding unknown/No results)
    found_expressions = {}
    for word, level in word_levels:
        if level not in ["A0", "No results"]:
            if level not in found_expressions:
                found_expressions[level] = []
            if word not in found_expressions[level]:  # Avoid duplicates
                found_expressions[level].append(word)
    
    # Sort expressions within each level
    for level in found_expressions:
        found_expressions[level].sort()
    
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
        "found_expressions": found_expressions,
    }
    return result, word_level_dict
