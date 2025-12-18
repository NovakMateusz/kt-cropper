from pathlib import Path

import fitz
from PIL import Image

from cropper.models import Resource, Resources, ImageFormat, CropBox


class CroppedImage:
    def __init__(self, image: Image, name: str):
        self.image = image
        self.name = name

    def save(self, output_dir: Path, format: str):
        self.image.save(output_dir / f"{self.name}.{format}")


def handle_request(
    pdf_path: Path,
    resources: Resources,
    dpi: int,
    format: ImageFormat,
    output_dir: Path,
):
    document = fitz.open(pdf_path)
    zoom = dpi / 72

    for resource in resources:
        for image in get_resource(document, resource, zoom):
            image.save(output_dir=output_dir, format=format)


def get_resource(doc, resource, zoom):
    matrix = fitz.Matrix(zoom, zoom)
    for page_n in range(resource.pages.start, resource.pages.stop):
        page = doc[page_n]
        pixmap = page.get_pixmap(matrix=matrix)
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

        for i, crop_box in enumerate(resource.crop_boxes):
            imag_name = f"page_{page_n}_{resource.name}_{i}"
            yield CroppedImage(image=crop_image(crop_box, image, zoom), name=imag_name)


def crop_image(crop_box, image, zoom) -> Image:
    crop_scaled = (
        int(crop_box[0] * zoom),
        int(crop_box[1] * zoom),
        int(crop_box[2] * zoom),
        int(crop_box[3] * zoom),
    )
    return image.crop(crop_scaled)
