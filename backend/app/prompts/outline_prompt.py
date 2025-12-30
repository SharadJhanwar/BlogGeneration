from langchain_core.prompts import PromptTemplate

outline_prompt = PromptTemplate(
    input_variables=["title", "keywords", "tone"],
    template="""
    Create a comprehensive and detailed blog outline for the following topic.

    Title: {title}
    Tone: {tone}
    Keywords: {keywords}

    Output Format:
    [SECTION] Main Title
    [SUBTOPIC] Specific point
    [SUBTOPIC] Specific point
    [SECTION] Next Main Title
    ...
    
    DO NOT use actual numbers (1, 2, 3). Use the labels above.
    """
)
