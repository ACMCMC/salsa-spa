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
    
    # Use moderate weighting for higher levels (tail of distribution)
    # Balanced approach: use level^1.02 for a very gentle boost to advanced words
    # This gives C2 ~1.2x weight vs A1, which is a reasonable middle ground
    # Advanced words matter slightly more but don't dominate the calculation
    poly_weights = {lvl: (level_values[lvl] ** 1.02) for lvl in known_levels}
    
    # Calculate grade based only on known words, with heavy tail weighting
    present_levels = [
        lvl for lvl in known_levels if probabilities_known[lvl] > 0
    ]
    
    if present_levels:
        # Calculate weighted average of level values, with moderate boost for higher levels
        # Weight the probabilities (not the level values) to give advanced words more influence
        # This is a more balanced approach
        numerator = sum(
            (probabilities_known[lvl] * poly_weights[lvl]) * level_values[lvl]
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
    
    # Convert grade (0-1) to CEFR level prediction
    # Map grade to CEFR levels: 0=A0, 0-1/6=A1, 1/6-2/6=A2, 2/6-3/6=B1, 3/6-4/6=B2, 4/6-5/6=C1, 5/6-1.0=C2
    if grade == 0.0:
        predicted_level = "A0"
    elif grade <= 1/6:
        predicted_level = "A1"
    elif grade <= 2/6:
        predicted_level = "A2"
    elif grade <= 3/6:
        predicted_level = "B1"
    elif grade <= 4/6:
        predicted_level = "B2"
    elif grade <= 5/6:
        predicted_level = "C1"
    else:
        predicted_level = "C2"
    
    # Calculate confidence score (0-1)
    # Confidence is based on:
    # 1. Proportion of known words (more known words = higher confidence)
    # 2. Concentration of distribution (more concentrated = higher confidence)
    # 3. Sample size (more words = higher confidence, up to a point)
    
    if known_words_count == 0:
        confidence = 0.0
    else:
        # Base confidence on proportion of known words
        known_ratio = known_words_count / total_words if total_words > 0 else 0.0
        
        # Calculate concentration: how much probability is in the top level(s)
        # Use entropy-like measure: lower entropy = higher concentration = higher confidence
        if present_levels:
            # Calculate weighted entropy (lower = more concentrated)
            entropy = -sum(
                p * math.log(p + 1e-10)  # Add small epsilon to avoid log(0)
                for p in probabilities_known.values()
                if p > 0
            )
            max_entropy = math.log(len(present_levels)) if len(present_levels) > 1 else 1.0
            concentration = 1.0 - (entropy / max_entropy) if max_entropy > 0 else 1.0
        else:
            concentration = 0.0
        
        # Sample size factor: more words = higher confidence, but with diminishing returns
        # Use log scale: log(known_words + 1) / log(50 + 1) caps at ~50 words
        sample_factor = min(math.log(known_words_count + 1) / math.log(51), 1.0)
        
        # Combine factors: known_ratio (40%), concentration (40%), sample_factor (20%)
        confidence = (
            0.4 * known_ratio +
            0.4 * concentration +
            0.2 * sample_factor
        )
        confidence = min(max(confidence, 0.0), 1.0)  # Clamp to [0, 1]
    
    # Main output dict
    result = {
        "grade": grade,
        "predicted_level": predicted_level,
        "confidence": confidence,
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
