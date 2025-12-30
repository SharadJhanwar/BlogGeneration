from fastapi import APIRouter
from app.schemas.blog2 import Blog2Request
from app.services.blog2_service import generate_blog_v2

router = APIRouter(prefix="/api/v1")

@router.post("/generateBlog2")
def generate_blog(data: Blog2Request):
    print("Request Recieved For : ", data)
    return generate_blog_v2(data)
