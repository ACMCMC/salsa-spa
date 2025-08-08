"""
Text cleaning utilities for Spanish text analysis.
"""

import re
import unicodedata
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def clean_text(text: str) -> str:
    # Lowercase, remove accents, remove punctuation
    text = text.lower()
    text = "".join(
        char
        for char in unicodedata.normalize("NFD", text)
        if unicodedata.category(char) != "Mn"
    )
    text = re.sub(r"[^\w\s]", "", text)
    return text


def clean_word(word: str) -> str:
    # Lowercase and remove accents using Unicode normalization
    word = word.lower()
    word = "".join(
        char
        for char in unicodedata.normalize("NFD", word)
        if unicodedata.category(char) != "Mn"
    )
    return word
