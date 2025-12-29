from pydantic import BaseModel

class BlogRequest(BaseModel):
    title: str
    tone: str
    language: str
