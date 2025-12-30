from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.config.llm import  llm

prompt = PromptTemplate(
    input_variables=["outline", "language", "context"],
    template="""
Write blog sections based on the outline.

Outline:
{outline}

Context:
{context}

Language:
{language}

Rules:
- RETURN ONLY THE CONTENT: Do NOT include any intro, outro, or conversational meta-text.
- STRICT ADHERENCE: Write sections that strictly follow the Title and Outline.
- FILTER NOISE: Do NOT include any information from the context that is not directly related to the topic.
- WEB ACCESSIBILITY: Use proper semantic HTML (<h2>, <p>). Do NOT use markdown.
- Expand only on the relevant facts found in the context.
"""
)

section_chain = prompt | llm | StrOutputParser()
