"""
Word level detection logic for Spanish text analysis.
"""

import re
import logging
from .text_cleaning import clean_text, lemmatize_word
from .vocab_lists import level_dict_by_length

logging.basicConfig(level=logging.INFO, format="%(message)s")

# CEFR level order (highest to lowest)
LEVEL_ORDER = ["C2", "C1", "B2", "B1", "A2", "A1", "A0"]


def detect_word_levels(
    text: str, level_dictionary: dict[str, set[str]]
) -> list[tuple[str, str]]:
    """
    Detect word levels based on predefined word lists.
    Matches full expressions only - no partial matches allowed.
    """
    # Extract words from cleaned text (preserving order and positions)
    cleaned = clean_text(text=text)
    words = re.findall(r"\b\w+\b", cleaned)
    
    if not words:
        return []
    
    # Find maximum expression length in vocabulary
    max_length = 1
    for level, length_dict in level_dict_by_length.items():
        if length_dict:
            max_length = max(max_length, max(length_dict.keys()))
    
    result = []
    i = 0
    
    # Process words sequentially, trying longest matches first
    while i < len(words):
        matched = False
        
        # Try matching expressions from longest to shortest starting at position i
        for n in range(min(max_length, len(words) - i), 0, -1):
            # Extract n-gram
            ngram_words = words[i:i + n]
            ngram_text = " ".join(ngram_words)
            
            # Lemmatize the n-gram
            lemmatized_ngram = lemmatize_word(ngram_text)
            
            # Try to match against vocabulary of the same length
            # Check levels from highest to lowest to prioritize higher levels
            for level in LEVEL_ORDER:
                if level in level_dict_by_length:
                    length_dict = level_dict_by_length[level]
                    if n in length_dict and lemmatized_ngram in length_dict[n]:
                        # Full match found at this level
                        result.append((ngram_text, level))
                        i += n  # Skip all words in this expression
                        matched = True
                        break
            
            if matched:
                break
        
        if not matched:
            # No match found for word at position i
            result.append((words[i], "No results"))
            i += 1
    
    return result
