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


class Scope(BaseModel):
    start_page: NonNegativeInt
    stop_page: NonNegativeInt


class Extraction(BaseModel):
    name: str
    scope: Scope
    crop_boxes: List[CropBox]


Extractions = List[Extraction]


class CropManifest(BaseModel):
    team_name: str
    extractions: Extractions
