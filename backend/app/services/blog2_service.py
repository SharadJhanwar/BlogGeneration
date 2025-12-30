from app.chains.blog2_pipeline import blog2_pipeline

def generate_blog_v2(data):
    return blog2_pipeline({
        "title": data.title,
        "tone": data.tone,
        "language": data.language
    })
