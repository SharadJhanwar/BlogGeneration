from fastapi import APIRouter
from app.schemas.blog import BlogRequest
from app.services.llm_service import generate_blog

router = APIRouter(prefix="/api/v1", tags=["Blog"])

@router.post("/generateBlog")
def generate_blog_api(data: BlogRequest):
  return generate_blog(data)