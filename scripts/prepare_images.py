"""Prepare field survey photos for publication.

Reads data/field_survey.csv, removes all EXIF metadata from each photo,
resizes it to at most 1600px on its longest side and saves it to
docs/field-survey/images/ as 'YYYY-MM-DD_NN_slug.jpg'.

Usage:
    python scripts/prepare_images.py
"""

import csv
from pathlib import Path

from PIL import Image, ImageOps

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "data" / "field_survey.csv"
OUTPUT_DIR = PROJECT_ROOT / "docs" / "field-survey" / "images"
MAX_SIZE = 1600
JPEG_QUALITY = 85


def main():
    """Process every photo listed in the field survey CSV."""
    rows = read_survey(CSV_PATH)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    counters = {}

    for row in rows:
        date = row["date"]
        counters[date] = counters.get(date, 0) + 1
        name = build_output_name(date, counters[date], row["slug"])
        source = PROJECT_ROOT / row["original_file"]
        target = OUTPUT_DIR / name
        prepare_image(source, target)
        print(f"{source.name} -> {target.name}")


def read_survey(path):
    """Return the CSV rows as a list of dicts."""
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def build_output_name(date, number, slug):
    """Return a file name like '2026-05-27_01_open-canal.jpg'."""
    return f"{date}_{number:02d}_{slug}.jpg"


def prepare_image(source, target, max_size=MAX_SIZE):
    """Save a resized copy of source at target without any metadata."""
    with Image.open(source) as image:
        image = ImageOps.exif_transpose(image)
        image = image.convert("RGB")
        image.thumbnail((max_size, max_size))

        clean = Image.new("RGB", image.size)
        clean.paste(image)
        clean.save(target, "JPEG", quality=JPEG_QUALITY)


if __name__ == "__main__":
    main()
