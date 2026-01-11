from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="GenAI blog generation")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# import api routers
from app.api.v1.blog import router as blog_router
from app.api.v1.blog2 import router as blog2_router
from app.api.v1.blog3 import router as blog3_router
from app.api.v1.images import router as images_router
from app.api.v1.export import router as export_router

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
app.include_router(blog2_router)
app.include_router(blog3_router)
app.include_router(images_router)
app.include_router(export_router)