from typing import Generator
from pathlib import Path

import fitz
from PIL import Image
from pymupdf import Document

from kt_cropper.models import Extraction, Extractions, ImageFormat, CropBox
from kt_cropper.utils.logger import get_logger

logger = get_logger(__name__)


class CroppedImage:
    def __init__(self, image: Image, name: str):
        self.image = image
        self.name = name

    def save(self, output_dir: Path, format: str):
        file_name = output_dir / f"{self.name}.{format}"
        logger.info("saving image to %s", file_name)
        self.image.save(file_name)


def process_pdf_extractions(
    pdf_path: Path, extractions: Extractions, dpi: int, format: ImageFormat, output_dir: Path
):
    """
    Coordinates the extraction of images according to the provided definitions.

    This function opens the given PDF document and orchestrates the extraction of images
    based on the provided instructions. Extracted images are saved to the output directory
    in the requested image format.
    """
    logger.debug("Opening PDF document under %s" % pdf_path)
    document = fitz.open(pdf_path)
    logger.debug("Calculating zoom")
    zoom = dpi / 72

    for extraction in extractions:
        logger.debug("Performing extraction for %s" % extraction.name)
        for image in extract_image(document, extraction, zoom):
            image.save(output_dir=output_dir, format=format)
        logger.debug("Extraction for %s is done" % extraction.name)


def extract_image(
    document: Document, extraction: Extraction, zoom: float
) -> Generator[CroppedImage, None, None]:
    """
    Extract cropped images from a PDF document based on an extraction definition.

    Generator that iterates over the pages defined in the extraction scope, renders each page
    into a raster image using the provided zoom factor (derived from DPI), and applies all
    configured crop boxes to the rendered page.
    """
    matrix = fitz.Matrix(zoom, zoom)
    for page_number in range(extraction.scope.start_page, extraction.scope.stop_page):
        page = document[page_number]
        logger.debug("Getting raw pixel buffer")
        pixmap = page.get_pixmap(matrix=matrix)  # Longest running part
        logger.debug("Converting the raw pixel buffer into a Pillow Image")
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

        for i, crop_box in enumerate(extraction.crop_boxes, start=1):
            imag_name = f"page_{page_number + 1}_{extraction.name}_{i}"
            yield CroppedImage(image=crop_image(crop_box, image, zoom), name=imag_name)


def crop_image(crop_box: CropBox, image: Image, zoom: float) -> Image:
    """
    Crop a region from a rendered PDF page image using PDF point coordinates.

    The crop box is defined in PDF points (1/72 inch) and is scaled to pixel coordinates using
    the provided zoom factor before cropping. The function returns a new Pillow Image containing
    the cropped region.
    """
    crop_scaled = (
        int(crop_box[0] * zoom),
        int(crop_box[1] * zoom),
        int(crop_box[2] * zoom),
        int(crop_box[3] * zoom),
    )
    return image.crop(crop_scaled)
