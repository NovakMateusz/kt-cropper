from typing import Generator
from pathlib import Path

import fitz
from PIL import Image
from pymupdf import Document

from cropper.models import Extraction, Extractions, ImageFormat, CropBox
from cropper.utils.logger import get_logger

logger = get_logger(__name__)


class CroppedImage:
    def __init__(self, image: Image, name: str):
        self.image = image
        self.name = name

    def save(self, output_dir: Path, format: str):
        file_name = output_dir / f"{self.name}.{format}"
        logger.info("saving image to %s", file_name)
        self.image.save(file_name)


def handle_request(
    pdf_path: Path, extractions: Extractions, dpi: int, format: ImageFormat, output_dir: Path
):
    logger.debug("Opening PDF document under %s" % pdf_path)
    document = fitz.open(pdf_path)
    logger.debug("Calculating zoom")
    zoom = dpi / 72

    for extraction_info in extractions:
        logger.debug("Performing extraction for %s" % extraction_info.name)
        for image in extract_image(document, extraction_info, zoom):
            image.save(output_dir=output_dir, format=format)


def extract_image(
    document: Document, extraction: Extraction, zoom: float
) -> Generator[CroppedImage, None, None]:
    matrix = fitz.Matrix(zoom, zoom)
    for page_number in range(extraction.scope.start_page, extraction.scope.stop_page):
        page = document[page_number]
        pixmap = page.get_pixmap(matrix=matrix)
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

        for i, crop_box in enumerate(extraction.crop_boxes, start=1):
            imag_name = f"page_{page_number + 1}_{extraction.name}_{i}"
            yield CroppedImage(image=crop_image(crop_box, image, zoom), name=imag_name)


def crop_image(crop_box: CropBox, image: Image, zoom: float) -> Image:
    crop_scaled = (
        int(crop_box[0] * zoom),
        int(crop_box[1] * zoom),
        int(crop_box[2] * zoom),
        int(crop_box[3] * zoom),
    )
    return image.crop(crop_scaled)
