from langchain_core.prompts import PromptTemplate

section_prompt = PromptTemplate(
    input_variables=["outline", "language"],
    template="""
    Role: Professional Blog Architect (HTML Specialist)
    Objective: Transform the provided outline into a perfectly structured HTML blog post.
    
    Outline:
    {outline}

    Language: {language}

    STRICT ARCHITECTURAL RULES:
    1. Every main section from the outline MUST start with an <h2> tag.
    2. Every sub-topic MUST start with an <h3> tag.
    3. Every block of descriptive text MUST be wrapped in <p> tags.
    4. NO text is allowed outside of <p>, <h2>, <h3>, <ul>, or <li> tags.
    5. NO Markdown characters (#, *, -) allowed.
    6. Double check: Ensure paragraphs are distinct <p> blocks and headers are distinct <h2>/<h3> blocks.

    EXAMPLE MAPPING:
    Outline: - Introduction
    HTML: <h2>Introduction</h2><p>Content goes here...</p>

    Outline: - Benefits of AI
    HTML: <h2>Benefits of AI</h2><p>Content...</p>
    """
)
