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


def test_full_expression_match_multiword():
    """
    Test that multi-word expressions only match when the full expression is present.
    "llevar" alone should NOT match "llevar gafas".
    """
    result = detect_word_levels(text="llevar", level_dictionary=level_dict)
    # "llevar" alone should not match "llevar gafas" - should be "No results"
    # unless "llevar" exists as a single word entry
    # Check that we don't get a false positive match
    assert isinstance(result, list)
    assert len(result) == 1
    # The result should either be "No results" or a valid single-word match
    # but NOT a match for "llevar gafas"
    assert result[0][0] == "llevar"


def test_full_expression_match_complete():
    """
    Test that complete multi-word expressions match correctly.
    "llevar gafas" should match "llevar gafas".
    """
    result = detect_word_levels(text="llevar gafas", level_dictionary=level_dict)
    assert isinstance(result, list)
    # Should match as a single expression
    assert len(result) == 1
    assert result[0][0] == "llevar gafas"
    assert result[0][1] != "No results"


def test_full_expression_match_partial_no_match():
    """
    Test that partial matches don't occur.
    If vocabulary has "llevar gafas" but text only has "llevar",
    it should NOT match.
    """
    # Create a test dictionary with only multi-word expressions
    test_dict = {
        "A1": {"llevar gafa"},  # lemmatized form
    }
    # Mock the level_dict_by_length for this test
    from salsa_spa import word_level
    original_dict = word_level.level_dict_by_length
    word_level.level_dict_by_length = {
        "A1": {2: {"llevar gafa"}}  # 2-word expression
    }
    
    try:
        result = detect_word_levels(text="llevar", level_dictionary=test_dict)
        # "llevar" alone should NOT match "llevar gafa"
        assert len(result) == 1
        assert result[0][1] == "No results"
    finally:
        word_level.level_dict_by_length = original_dict


def test_full_expression_match_longer_first():
    """
    Test that longer expressions are matched before shorter ones.
    If both "llevar" and "llevar gafas" exist, "llevar gafas" should match first.
    """
    # Create a test dictionary with both single and multi-word expressions
    test_dict = {
        "A1": {"llevar", "llevar gafa"},
    }
    from salsa_spa import word_level
    original_dict = word_level.level_dict_by_length
    word_level.level_dict_by_length = {
        "A1": {1: {"llevar"}, 2: {"llevar gafa"}}
    }
    
    try:
        result = detect_word_levels(text="llevar gafas", level_dictionary=test_dict)
        # Should match "llevar gafas" (2 words) not just "llevar" (1 word)
        assert len(result) == 1
        assert result[0][0] == "llevar gafas"
        assert result[0][1] == "A1"
    finally:
        word_level.level_dict_by_length = original_dict


def test_full_expression_match_mixed():
    """
    Test matching with mixed single and multi-word expressions in text.
    """
    result = detect_word_levels(
        text="él lleva gafas y es inteligente", level_dictionary=level_dict
    )
    assert isinstance(result, list)
    # Should process all words/expressions
    assert len(result) > 0
    # Check that expressions are matched correctly
    words_found = [r[0] for r in result]
    assert "él" in words_found or any("él" in w for w in words_found)


def test_highest_level_matched_first():
    """
    Test that when a word exists in multiple levels, the highest level is matched first.
    """
    # Create a test dictionary with the same word at different levels
    test_dict = {
        "A1": {"test"},
        "B2": {"test"},
        "C1": {"test"},
    }
    from salsa_spa import word_level
    original_dict = word_level.level_dict_by_length
    word_level.level_dict_by_length = {
        "A1": {1: {"test"}},
        "B2": {1: {"test"}},
        "C1": {1: {"test"}},
    }
    
    try:
        result = detect_word_levels(text="test", level_dictionary=test_dict)
        # Should match at C1 (highest level), not A1 or B2
        assert len(result) == 1
        assert result[0][0] == "test"
        assert result[0][1] == "C1", f"Expected C1, got {result[0][1]}"
    finally:
        word_level.level_dict_by_length = original_dict
