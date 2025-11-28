"""
File I/O utilities for reading and writing text and CSV files.
"""

import csv
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(message)s")


def read_text_file(filepath: str) -> Optional[str]:
    # Read and return the content of a text file
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        return None


def write_text_file(filepath: str, content: str) -> None:
    # Write content to a text file
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
        logging.info(f"Text saved to: {filepath}")
    except Exception as e:
        logging.error(f"Error writing file: {e}")


def export_to_csv(data: list[tuple[str, str]], output_path: str) -> None:
    # Export results to a CSV file
    try:
        with open(output_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Word", "CEFR Level"])
            writer.writerows(data)
        logging.info(f"Results saved to {output_path}")
    except Exception as e:
        logging.error(f"Error exporting CSV: {e}")
