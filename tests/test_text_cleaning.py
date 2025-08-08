"""
Tests for salsa_spa/text_cleaning.py utilities.
"""

from salsa_spa.text_cleaning import clean_text, clean_word


def test_clean_text_basic():
    assert clean_text(text="Árbol, café!") == "arbol cafe"


def test_clean_word_basic():
    assert clean_word(word="niño") == "nino"


def test_clean_text_punctuation():
    assert clean_text(text="¿Qué hora es?") == "que hora es"


def test_clean_word_accents():
    assert clean_word(word="acción") == "accion"
