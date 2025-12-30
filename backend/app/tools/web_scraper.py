from langchain_core.tools import tool
from langchain_community.document_loaders import WebBaseLoader

@tool
def web_scraper(url: str) -> str:
    """
    Scrape and extract readable text from a webpage URL.
    """
    loader = WebBaseLoader(url)
    docs = loader.load()
    return docs[0].page_content[:4000]
