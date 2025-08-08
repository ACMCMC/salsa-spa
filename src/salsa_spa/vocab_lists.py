"""
Vocabulary lists loader for salsa-spa.
Loads CEFR word lists from a CSV file.
"""

import csv
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

VOCAB_CSV_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "vocab", "all_vocab_levels.csv")
)

level_dict: dict[str, set[str]] = {}

try:
    with open(VOCAB_CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            word = row["word"]
            level = row["level"]
            if level not in level_dict:
                level_dict[level] = set()
            level_dict[level].add(word)
except Exception as e:
    logging.error(f"Error loading vocabulary CSV: {e}")
    raise

# level_dict: { 'A1': set([...]), 'A2': set([...]), ... }
