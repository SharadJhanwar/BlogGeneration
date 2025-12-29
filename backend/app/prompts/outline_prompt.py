from langchain_core.prompts import PromptTemplate

outline_prompt = PromptTemplate(
    input_variables=["title", "keywords", "tone"],
    template="""
    Create a detailed blog outline.

    Title: {title}
    Tone: {tone}
    Keywords: {keywords}

    Use H2 and H3 headings.
    """
)
