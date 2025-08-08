"""
Tests for the salsa-spa CLI using Typer's test client.
"""

import os
import sys
import logging
from typer.testing import CliRunner
from salsa_spa.cli import app

runner = CliRunner()


def test_grade_file(tmp_path):
    # Create a temporary text file
    test_file = tmp_path / "test.txt"
    test_file.write_text("bailar con el presidente")
    output_csv = tmp_path / "test.csv"

    assert test_file.exists(), "Test file does not exist!"

    # Typer expects options before positional arguments
    result = runner.invoke(
        app, ["grade-file", "--filepath", str(test_file), "--output", str(output_csv)]
    )
    assert result.exit_code == 0
    assert output_csv.exists()
    # Check output CSV content
    import csv

    rows = list(csv.reader(output_csv.open()))
    assert any("bailar" in row for row in rows)
    assert any("presidente" in row for row in rows)


def test_grade_text(tmp_path):
    output_json = tmp_path / "text_result.json"
    result = runner.invoke(
        app,
        [
            "grade-text",
            "--text",
            "bailar con el presidente",
            "--output",
            str(output_json),
        ],
    )
    assert result.exit_code == 0
    assert output_json.exists()
    import json

    content = json.loads(output_json.read_text())
    assert "probabilities" in content
    # Check that input text words are present in the output if needed
