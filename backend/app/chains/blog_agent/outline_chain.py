from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.config.llm import  llm

prompt = PromptTemplate(
    input_variables=["title", "tone", "keywords", "context"],
    template="""
Create a detailed blog outline.

Title:
{title}

Tone:
{tone}

Keywords:
{keywords}

Context:
{context}

Rules:
- STRICT ALIGNMENT: The outline must follow the Title strictly.
- CONTENT FILTERING: Ignore any information in the context that is unrelated to the Title.
- LOGICAL STRUCTURE: Create a coherent flow from introduction to conclusion.
"""
)

outline_chain = prompt | llm | StrOutputParser()
