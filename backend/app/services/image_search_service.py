import os
import requests
from app.chains.outline_chain import outline_chain
from app.chains.image_topic_chain import image_topic_chain

def search_unsplash(query, count=5):
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    if not access_key:
        return []
    
    url = f"https://api.unsplash.com/search/photos?query={query}&per_page={count}"
    headers = {"Authorization": f"Client-ID {access_key}"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            results = response.json().get("results", [])
            return [
                {
                    "url": img["urls"]["regular"],
                    "thumb": img["urls"]["thumb"],
                    "source": "Unsplash",
                    "photographer": img["user"]["name"],
                    "link": img["links"]["html"]
                }
                for img in results
            ]
    except Exception as e:
        print(f"Unsplash error: {e}")
    return []

def search_pexels(query, count=5):
    api_key = os.getenv("PEXELS_API_KEY")
    if not api_key:
        return []
    
    url = f"https://api.pexels.com/v1/search?query={query}&per_page={count}"
    headers = {"Authorization": api_key}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            photos = response.json().get("photos", [])
            return [
                {
                    "url": img["src"]["landscape"],
                    "thumb": img["src"]["tiny"],
                    "source": "Pexels",
                    "photographer": img["photographer"],
                    "link": img["url"]
                }
                for img in photos
            ]
    except Exception as e:
        print(f"Pexels error: {e}")
    return []

def generate_images_service(data):
    # 1. Generate Outline
    outline = outline_chain.invoke({
        "title": data.title,
        "keywords": getattr(data, "keywords", ""),
        "tone": getattr(data, "tone", "professional")
    })
    
    # 2. Generate Image Topics from Outline
    topics_raw = image_topic_chain.invoke({
        "outline": outline,
        "title": data.title
    })
    topics = [t.strip("- ").strip() for t in topics_raw.split("\n") if t.strip()]
    
    # 3. Search Images (taking first few topics to get a mix)
    all_images = []
    # Mix from different topics to get 10 images
    for i, topic in enumerate(topics[:3]):
        # Get 2 from Unsplash and 2 from Pexels for each of the first 3 topics
        all_images.extend(search_unsplash(topic, 2))
        all_images.extend(search_pexels(topic, 2))
    
    return {
        "outline": outline,
        "images": all_images[:10] # Ensure we return around 10
    }