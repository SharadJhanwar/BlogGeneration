from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel
from typing import Literal
from app.services.export_service import export_blog

router = APIRouter(prefix="/api/v1", tags=["export"])

class ExportRequest(BaseModel):
    content: str
    title: str = "blog_post"
    format: Literal["pdf", "docx", "md", "html"]

@router.post("/export")
async def export_endpoint(request: ExportRequest):
    try:
        data, media_type, filename = await export_blog(
            request.content, 
            request.title, 
            request.format
        )
        
        return Response(
            content=data,
            media_type=media_type,
            headers={
                "Content-Disposition": f'attachment; filename="{filename}"'
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
