"""
Command-line interface for salsa-spa using Typer.
"""

import os
import logging
import json
import typer
from .file_io import read_text_file, export_to_csv
from .word_level import detect_word_levels
from .vocab_lists import level_dict
from .grader_prob import grade_with_probabilities

app = typer.Typer()
logging.basicConfig(level=logging.INFO, format="%(message)s")


@app.command("grade-file")
def grade_file(
    filepath: str = typer.Option(
        ..., "--filepath", help="Path to the text file to grade"
    ),
    output: str = typer.Option(None, "--output", help="Path to save CSV output"),
) -> None:
    """
    Grade a text file and output results to console or CSV.
    """
    text = read_text_file(filepath=filepath)
    if text is None:
        logging.error(f"Could not read file: {filepath}")
        raise typer.Exit(code=2)

    word_levels = detect_word_levels(text=text, level_dictionary=level_dict)
    for word, level in word_levels:
        logging.info(f"{word}: {level}")

    if output is not None:
        export_to_csv(data=word_levels, output_path=output)
        logging.info(f"\n✅ Result saved to {output}")


@app.command("grade-text")
def grade_text(
    text: str = typer.Option(..., "--text", help="Text to grade"),
    output: str = typer.Option(None, "--output", help="Path to save JSON output"),
) -> None:
    """
    Grade a string of text and output results as JSON.
    """
    result, _ = grade_with_probabilities(text=text)
    if output is not None:
        with open(output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
    else:
        typer.echo(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    app()
