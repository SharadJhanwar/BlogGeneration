from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="GenAI blog generation")

# import api routers
from app.api.v1.blog import router as blog_router

@app.get("/")
def root():
  return {
    "message":"Welcome to genAI Blog Generation platform",
    "status":"ok"
  }

@app.get("/health")
def health_check():
  return{
    "status":"ok",
    "service":"fastapi-backend"
  }

app.include_router(blog_router)