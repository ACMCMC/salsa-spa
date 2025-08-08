"""
Tests for salsa_spa/word_level.py logic.
"""

from salsa_spa.word_level import detect_word_levels
from salsa_spa.vocab_lists import level_dict


def test_detect_word_levels_basic():
    result = detect_word_levels(
        text="bailar con el presidente", level_dictionary=level_dict
    )
    assert isinstance(result, list)
    assert all(len(t) == 2 for t in result)


def test_detect_word_levels_empty():
    result = detect_word_levels(text="", level_dictionary=level_dict)
    assert result == []


def test_detect_word_levels_no_results():
    result = detect_word_levels(text="xyzabc", level_dictionary=level_dict)
    assert result[0][1] == "No results"
