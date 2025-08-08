"""
Tests for grade_with_probabilities in grader_prob.py
"""

from salsa_spa.grader_prob import grade_with_probabilities
import pytest


@pytest.mark.parametrize(
    "level,word,expected_grade_range",
    [
        ("A0", "foo", (0.0, 0.0)),
        ("A1", "salida", (0.0, 1.0)),
        ("A2", "uniforme", (0.0, 1.0)),
        ("B1", "entrenador", (0.0, 1.0)),
        ("B2", "aliado", (0.0, 1.0)),
        ("C1", "edil", (0.0, 1.0)),
        ("C2", "cloroformo", (0.9, 1.0)),
    ],
)
def test_all_single_level(level, word, expected_grade_range):
    text = f"{word} {word} {word} {word}"
    result, _ = grade_with_probabilities(text=text)
    assert result["probabilities"][level] == 1.0
    assert expected_grade_range[0] <= result["grade"] <= expected_grade_range[1]


def test_all_c2():
    text = "cloroformo cloroformo cloroformo cloroformo"
    result, _ = grade_with_probabilities(text=text)
    assert result["probabilities"]["C2"] == 1.0
    assert result["grade"] == 1.0


def test_all_a0():
    text = "foo foo foo foo"
    result, _ = grade_with_probabilities(text=text)
    assert result["probabilities"]["A0"] == 1.0
    assert result["grade"] == 0.0
