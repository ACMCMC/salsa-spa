"""
Vocabulary lists loader for salsa-spa.
Loads CEFR word lists from a CSV file and lemmatizes them.
Uses a cache file to avoid reprocessing on every import.
"""

import csv
import os
import logging
import pickle
from typing import Optional, Tuple
from .text_cleaning import lemmatize_word

logging.basicConfig(level=logging.INFO, format="%(message)s")

VOCAB_CSV_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "vocab", "all_vocab_levels.csv")
)

# Cache file path (hidden file in the vocab directory)
CACHE_DIR = os.path.dirname(VOCAB_CSV_PATH)
CACHE_FILE = os.path.join(CACHE_DIR, ".vocab_cache.pkl")

level_dict: dict[str, set[str]] = {}
# Dictionary organized by expression length for efficient matching
level_dict_by_length: dict[str, dict[int, set[str]]] = {}


def _load_from_cache() -> Optional[Tuple[dict[str, set[str]], dict[str, dict[int, set[str]]]]]:
    """Load processed vocabulary from cache if it exists and is valid."""
    if not os.path.exists(CACHE_FILE):
        return None
    
    try:
        # Check if cache is newer than CSV
        cache_mtime = os.path.getmtime(CACHE_FILE)
        csv_mtime = os.path.getmtime(VOCAB_CSV_PATH)
        
        if cache_mtime < csv_mtime:
            # CSV is newer, cache is invalid
            logging.info("Vocabulary CSV is newer than cache, will reprocess...")
            return None
        
        # Load from cache
        with open(CACHE_FILE, "rb") as f:
            cached_data = pickle.load(f)
            return cached_data.get("level_dict"), cached_data.get("level_dict_by_length")
    except Exception as e:
        logging.warning(f"Error loading cache: {e}. Will reprocess vocabulary.")
        return None


def _save_to_cache(level_dict: dict[str, set[str]], level_dict_by_length: dict[str, dict[int, set[str]]]) -> None:
    """Save processed vocabulary to cache."""
    try:
        cached_data = {
            "level_dict": level_dict,
            "level_dict_by_length": level_dict_by_length,
        }
        with open(CACHE_FILE, "wb") as f:
            pickle.dump(cached_data, f)
        logging.info(f"Vocabulary cache saved to {CACHE_FILE}")
    except Exception as e:
        logging.warning(f"Error saving cache: {e}")


def _process_vocabulary() -> Tuple[dict[str, set[str]], dict[str, dict[int, set[str]]]]:
    """Process vocabulary CSV and return processed dictionaries."""
    level_dict_result: dict[str, set[str]] = {}
    level_dict_by_length_result: dict[str, dict[int, set[str]]] = {}
    
    logging.info("Processing vocabulary CSV (this may take a moment)...")
    with open(VOCAB_CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            word = row["word"]
            level = row["level"]
            # Lemmatize the word before adding to dictionary
            lemmatized_word = lemmatize_word(word)
            if level not in level_dict_result:
                level_dict_result[level] = set()
            level_dict_result[level].add(lemmatized_word)
            
            # Also organize by length for efficient matching
            if level not in level_dict_by_length_result:
                level_dict_by_length_result[level] = {}
            word_count = len(lemmatized_word.split())
            if word_count not in level_dict_by_length_result[level]:
                level_dict_by_length_result[level][word_count] = set()
            level_dict_by_length_result[level][word_count].add(lemmatized_word)
    
    logging.info("Vocabulary processing complete.")
    return level_dict_result, level_dict_by_length_result


# Load vocabulary (from cache if available, otherwise process and cache)
try:
    cached_result = _load_from_cache()
    if cached_result is not None:
        level_dict, level_dict_by_length = cached_result
        logging.info("Vocabulary loaded from cache.")
    else:
        level_dict, level_dict_by_length = _process_vocabulary()
        _save_to_cache(level_dict, level_dict_by_length)
except Exception as e:
    logging.error(f"Error loading vocabulary: {e}")
    raise

# level_dict: { 'A1': set([...]), 'A2': set([...]), ... }
# level_dict_by_length: { 'A1': {1: set([...]), 2: set([...]), ...}, ... }
# All words in the dictionary are lemmatized
