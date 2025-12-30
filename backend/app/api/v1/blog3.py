from fastapi import APIRouter
from app.schemas.blog import BlogRequest
from app.services.blog3_service import generate_blog_v3

router = APIRouter(prefix="/api/v1")

@router.post("/generateBlog3")
def generate_blog(data: BlogRequest):
    print("Request Recieved For : ", data)
    return generate_blog_v3(data)  