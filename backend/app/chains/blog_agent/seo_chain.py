from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.config.llm import  llm

prompt = PromptTemplate(
    input_variables=["content", "keywords", "context"],
    template="""
Improve SEO and readability.

Content:
{content}

Keywords:
{keywords}

Context:
{context}

Rules:
- RETURN ONLY THE CONTENT: Do NOT include any preamble (e.g., "Here is the revised version..."), postamble, or metadata.
- NO KEYWORDS LIST: Do NOT append keywords at the end of the content.
- Optimize for the specific Topic and Keywords while maintaining strict relevance.
- Maintain meaning and factual accuracy.
"""
)

seo_chain = prompt | llm | StrOutputParser()
