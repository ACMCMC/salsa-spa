"""
Tests for salsa_spa.file_io module.
"""

import os
from salsa_spa.file_io import write_text_file, read_text_file, export_to_csv


def test_write_and_read_text_file(tmp_path):
    test_file = tmp_path / "test_write.txt"
    write_text_file(filepath=str(test_file), content="árbol")
    content = read_text_file(filepath=str(test_file))
    assert content == "árbol"


def test_export_to_csv(tmp_path):
    test_csv = tmp_path / "test.csv"
    data = [("bailar", "A1"), ("presidente", "B2")]
    export_to_csv(data=data, output_path=str(test_csv))
    assert test_csv.exists()
    content = test_csv.read_text()
    assert "bailar" in content
    assert "presidente" in content
