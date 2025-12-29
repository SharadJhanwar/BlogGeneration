from langchain_core.prompts import PromptTemplate

keyword_prompt = PromptTemplate(
    input_variables=["title"],
    template="""
    Extract SEO keywords for the blog titled:
    "{title}"

    Return keywords as a comma-separated list.
    """
)
