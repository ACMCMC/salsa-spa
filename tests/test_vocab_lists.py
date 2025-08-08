"""
Tests for salsa_spa/vocab_lists.py loader.
"""

from salsa_spa.vocab_lists import level_dict


def test_vocab_loaded():
    # Should load levels and words
    assert isinstance(level_dict, dict)
    assert len(level_dict) > 0
    # Check at least one word in one level
    found = any(len(words) > 0 for words in level_dict.values())
    assert found
