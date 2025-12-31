from langchain_community.tools import DuckDuckGoSearchRun
from langchain_tavily import TavilySearch
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import time

load_dotenv()

def safe_tavily_search(query: str, retries: int = 2) -> str:
    search = TavilySearch()

    for attempt in range(retries):
        try:
            return search.invoke(query)
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2)  # wait before retry
            else:
                return f"No real-time search data available due to network timeout. Error: {e}"

def safe_duckduckgo_search(query: str, retries: int = 2) -> str:
    search = DuckDuckGoSearchRun()

    for attempt in range(retries):
        try:
            return search.invoke(query)
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2)  # wait before retry
            else:
                return f"No real-time search data available due to network timeout. Error: {e}"

def generate_seo_blog(topic: str, tone: str, language: str) -> str:
    # 1. Get real-time context safely
    # search_results = safe_duckduckgo_search(topic)
    search_results = safe_tavily_search(topic)

    # 2. Initialize LLM
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3
    )

    # 3. SEO + safety grounded prompt
    prompt = f"""
You are a professional SEO content writer.

Write an SEO-optimized blog post on the topic:
"{topic}"

Tone: {tone}
Language: {language}

Use the following real-time search context ONLY if it contains verified information:
{search_results}

Rules:
##IMPORTANT RULE -> If the topic is fundamentally invalid (e.g., a technology, event, or concept
did not exist in the specified year),
DO NOT reinterpret, reframe, or expand the topic into historical context.
Instead:
- Clearly state that the premise is incorrect
- Explain briefly why it is incorrect
- Stop the article there

- If the topic refers to a past year and that event hasn't occurred yet,
do NOT describe incidents as facts.
Instead, clearly state that the event is not valid
- If the topic refers to a future year ,
do NOT describe incidents as facts.
Instead, clearly state that the event has not occurred yet
and discuss it as a hypothetical, historical context, or risk analysis. (DONT Discuss ANY HYPOTHETICAL FOR PAST EVENTS UNLESS  ITS ASKED EXPLICITLY)
- Do NOT invent or assume facts
- If the search context does NOT confirm critical facts (such as deaths, events, or claims),
  clearly state that the information could not be verified
- Neutral, factual, responsible tone
- Suitable for publishing on a professional website
- If the topic is based on a false or unclear assumption, explain it responsibly

SEO Requirements:
- Start with an H1 title
- Provide a short section titled "Meta Description" using a <p> tag (DO NOT use <meta>)
- Use proper semantic HTML tags only:
  <h1>, <h2>, <h3>, <p>, <ul>, <li>, <strong>, <em>
- Do NOT use markdown
- Do NOT include <html>, <head>, <body>, or <meta> tags
- Output BODY CONTENT ONLY

Output only valid HTML content.
"""

    response = llm.invoke(prompt)
    print(response.content)
    return response.content


def generate_blog_v3(data):
    content = generate_seo_blog(data.title, data.tone, data.language)
    return {"content": content}