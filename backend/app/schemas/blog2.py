from pydantic import BaseModel

class Blog2Request(BaseModel):
    title: str
    tone: str
    language: str
