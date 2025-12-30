from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.config.llm import  llm

prompt = PromptTemplate(
    input_variables=["title", "context"],
    template="""
You are an SEO expert.

Title:
{title}

Context:
{context}

Instructions:
- Extract 5-8 SEO keywords that are CENTRAL to the Title.
- Use the context only to find supporting terms.
- Discard any information or terms not related to the Title.
- Return a comma-separated list.
"""
)

keyword_chain = prompt | llm | StrOutputParser()  
