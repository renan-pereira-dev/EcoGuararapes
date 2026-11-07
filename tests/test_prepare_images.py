"""Tests for scripts/prepare_images.py."""

import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from prepare_images import build_output_name, prepare_image  # noqa: E402

GPS_IFD = 0x8825
MAKE_TAG = 0x010F


def make_photo_with_exif(path, size=(3000, 2000)):
    """Create a JPEG with camera and GPS EXIF tags, like a phone photo."""
    exif = Image.Exif()
    exif[MAKE_TAG] = "TestPhone"
    exif[GPS_IFD] = {1: "S", 2: (8.0, 7.0, 0.0)}
    Image.new("RGB", size, "green").save(path, "JPEG", exif=exif)


def test_fixture_has_exif(tmp_path):
    """Sanity check: the fake photo really has EXIF before processing."""
    source = tmp_path / "source.jpg"
    make_photo_with_exif(source)
    with Image.open(source) as image:
        assert len(image.getexif()) > 0


def test_prepare_image_removes_exif(tmp_path):
    source = tmp_path / "source.jpg"
    target = tmp_path / "target.jpg"
    make_photo_with_exif(source)

    prepare_image(source, target)

    with Image.open(target) as image:
        assert len(image.getexif()) == 0
        assert "exif" not in image.info


def test_prepare_image_resizes_keeping_ratio(tmp_path):
    source = tmp_path / "source.jpg"
    target = tmp_path / "target.jpg"
    make_photo_with_exif(source, size=(3000, 2000))

    prepare_image(source, target)

    with Image.open(target) as image:
        assert image.size == (1600, 1067)


def test_prepare_image_keeps_small_images(tmp_path):
    source = tmp_path / "source.jpg"
    target = tmp_path / "target.jpg"
    make_photo_with_exif(source, size=(800, 600))

    prepare_image(source, target)

    with Image.open(target) as image:
        assert image.size == (800, 600)


def test_build_output_name():
    assert build_output_name("2026-05-27", 1, "open-canal") == (
        "2026-05-27_01_open-canal.jpg"
    )
