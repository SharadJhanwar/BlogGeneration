from langchain_core.prompts import PromptTemplate

section_prompt = PromptTemplate(
    input_variables=["outline", "language"],
    template="""
    Write a complete blog article based on the outline below.

    Outline:
    {outline}

    Language: {language}

    Output in Markdown.
    """
)
