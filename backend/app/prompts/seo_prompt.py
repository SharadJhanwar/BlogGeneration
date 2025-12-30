from langchain_core.prompts import PromptTemplate

seo_prompt = PromptTemplate(
    input_variables=["content", "keywords"],
    template="""
    Role: You are an HTML Optimizer.
    Task: Improve SEO and readability of the given HTML content.

    Keywords: {keywords}
    Content: {content}

    Rules:
    1. Output MUST be valid HTML fragments (<h2>, <p>, etc.).
    2. Do NOT use Markdown.
    3. If the input is plain text, convert it to semantic HTML (<h2> for headings, <p> for body).
    4. Do NOT include ```html``` or ```markdown``` fences.
    5. Return ONLY the filtered HTML code.
    6. Preserve all HTML structure while integrating keywords naturally.

    EXAMPLE:
    Input HTML: <h2>AI in 2024</h2><p>AI is growing fast.</p>
    Keywords: Innovation, Future
    Output HTML: <h2>AI Innovation in 2024</h2><p>The Future of AI is growing fast through constant innovation.</p>
    """
)
