from pydantic import BaseModel
from typing import List, Optional

class ImageResponse(BaseModel):
    url: str
    thumb: str
    source: str
    photographer: str
    link: str

class GenerateImagesResponse(BaseModel):
    outline: str
    images: List[ImageResponse]
