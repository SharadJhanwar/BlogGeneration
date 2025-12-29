from app.chains.blog_pipeline import blog_pipeline

def generate_blog(data):
  return blog_pipeline({
    "title":data.title,
    "tone":data.tone,
    "language":data.language
  })