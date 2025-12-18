from enum import StrEnum
from typing import Tuple, List
from pathlib import Path

from PIL import Image
from pydantic import BaseModel, NonNegativeInt, TypeAdapter


class ImageFormat(StrEnum):
    PNG = "PNG"
    JPG = "PNG"


CropBox = Tuple[
    NonNegativeInt,
    NonNegativeInt,
    NonNegativeInt,
    NonNegativeInt,
]


class Pages(BaseModel):
    start: NonNegativeInt
    stop: NonNegativeInt


class Resource(BaseModel):
    name: str
    pages: Pages
    crop_boxes: Tuple[CropBox, CropBox, CropBox, CropBox]


Resources = TypeAdapter(List[Resource])
