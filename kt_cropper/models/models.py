from enum import StrEnum
from typing import Tuple, List

from pydantic import BaseModel, NonNegativeInt, field_validator, ValidationInfo


class ImageFormat(StrEnum):
    PNG = "PNG"
    JPG = "JPG"


CropBox = Tuple[
    NonNegativeInt,
    NonNegativeInt,
    NonNegativeInt,
    NonNegativeInt,
]


class Scope(BaseModel):
    start_page: NonNegativeInt
    stop_page: NonNegativeInt

    @field_validator('stop_page', mode='after')
    @classmethod
    def check_stop_gt_start(cls, value: NonNegativeInt, info: ValidationInfo) -> str:
        if value < info.data['start_page']:
            raise ValueError('Page stop value must be greater than the page start value')
        return value


class Extraction(BaseModel):
    name: str
    scope: Scope
    crop_boxes: List[CropBox]


Extractions = List[Extraction]


class CropManifest(BaseModel):
    team_name: str
    extractions: Extractions
