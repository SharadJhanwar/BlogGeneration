from langchain_core.output_parsers import StrOutputParser
from app.prompts.seo_prompt import seo_prompt
from app.config.llm import  llm

seo_chain = seo_prompt | llm | StrOutputParser()
