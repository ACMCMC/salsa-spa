"""
Word level detection logic for Spanish text analysis.
"""

import re
import logging
from .text_cleaning import clean_text

logging.basicConfig(level=logging.INFO, format="%(message)s")


def detect_word_levels(
    text: str, level_dictionary: dict[str, set[str]]
) -> list[tuple[str, str]]:
    # Detect word levels based on predefined word lists
    words = re.findall(r"\b\w+\b", clean_text(text=text))
    result = []
    for word in words:
        found = False
        for level, word_set in level_dictionary.items():
            if word in word_set:
                result.append((word, level))
                found = True
                break
        if not found:
            result.append((word, "No results"))
    return result
