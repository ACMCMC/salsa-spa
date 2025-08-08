"""
Basic tests for salsa-spa package.
"""

import os
from salsa_spa.file_io import read_text_file
from salsa_spa.text_cleaning import clean_text, clean_word
from salsa_spa.word_level import detect_word_levels
from salsa_spa.vocab_lists import level_dict


def test_clean_text():
    text = "Árbol, café!"
    cleaned = clean_text(text=text)
    assert cleaned == "arbol cafe"


def test_clean_word():
    word = "niño"
    cleaned = clean_word(word=word)
    assert cleaned == "nino"


def test_detect_word_levels():
    text = "bailar con el presidente"
    result = detect_word_levels(text=text, level_dictionary=level_dict)
    # Should return levels for each word
    assert isinstance(result, list)
    assert all(len(t) == 2 for t in result)


def test_read_text_file(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("árbol")
    content = read_text_file(filepath=str(test_file))
    assert content == "árbol"
