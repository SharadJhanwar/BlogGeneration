from langchain_core.prompts import PromptTemplate

seo_prompt = PromptTemplate(
    input_variables=["content", "keywords"],
    template="""
    Improve SEO of the following content.

    Content:
    {content}

    Keywords:
    {keywords}

    Improve readability and keyword density.
    """
)
