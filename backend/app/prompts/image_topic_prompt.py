from langchain_core.prompts import PromptTemplate

image_topic_prompt = PromptTemplate(
    input_variables=["outline","title"],
    template="""
    Based on the following blog outline, generate 10 specific and descriptive image search keywords or short titles.
    These should be suitable for searching on stock photo sites like Unsplash or Pexels.
    Focus on visual elements that represent the key points of the outline.

    Outline:
    {outline}

    Title:
    {title}

    Output Format:
    - Keyword 1
    - Keyword 2
    ...
    
    Provide only the list of 10 keywords, one per line.
    """
)
