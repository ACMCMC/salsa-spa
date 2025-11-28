"""
Vocabulary lists loader for salsa-spa.
Loads CEFR word lists from a CSV file and lemmatizes them.
"""

import csv
import os
import logging
from .text_cleaning import lemmatize_word

logging.basicConfig(level=logging.INFO, format="%(message)s")

VOCAB_CSV_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "vocab", "all_vocab_levels.csv")
)

level_dict: dict[str, set[str]] = {}
# Dictionary organized by expression length for efficient matching
level_dict_by_length: dict[str, dict[int, set[str]]] = {}

try:
    with open(VOCAB_CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            word = row["word"]
            level = row["level"]
            # Lemmatize the word before adding to dictionary
            lemmatized_word = lemmatize_word(word)
            if level not in level_dict:
                level_dict[level] = set()
            level_dict[level].add(lemmatized_word)
            
            # Also organize by length for efficient matching
            if level not in level_dict_by_length:
                level_dict_by_length[level] = {}
            word_count = len(lemmatized_word.split())
            if word_count not in level_dict_by_length[level]:
                level_dict_by_length[level][word_count] = set()
            level_dict_by_length[level][word_count].add(lemmatized_word)
except Exception as e:
    logging.error(f"Error loading vocabulary CSV: {e}")
    raise

# level_dict: { 'A1': set([...]), 'A2': set([...]), ... }
# level_dict_by_length: { 'A1': {1: set([...]), 2: set([...]), ...}, ... }
# All words in the dictionary are lemmatized
