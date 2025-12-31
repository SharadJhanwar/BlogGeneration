from fastapi import APIRouter
from app.schemas.blog import BlogRequest
from app.schemas.image import GenerateImagesResponse
from app.services.image_search_service import generate_images_service

router = APIRouter(prefix="/api/v1", tags=["Images"])

@router.post("/generateImages", response_model=GenerateImagesResponse)
def generate_images_api(data: BlogRequest):
    return generate_images_service(data)