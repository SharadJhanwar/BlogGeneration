from app.chains.keyword_chain import keyword_chain
from app.chains.outline_chain import  outline_chain
from app.chains.seo_chain import seo_chain
from app.chains.section_chain import section_chain

def blog_pipeline(inputs: dict):
  
  # Step 1: Keywords
  keywords = keyword_chain.invoke({
    "title": inputs["title"]
  })

  # Step 2: Outline
  outline = outline_chain.invoke({
    "title": inputs["title"],
    "tone":inputs["tone"],
    "keywords":keywords
  })

  # Step 3: Sections
  content = section_chain.invoke({
    "outline":outline,
    "language":inputs["language"]
  })

  # Step 4: SEO 
  final_content = seo_chain.invoke({
    "content": content,
    "keywords":keywords
  })

  return {
    "keywords":keywords,
    "outline": outline,
    "content": final_content
  }