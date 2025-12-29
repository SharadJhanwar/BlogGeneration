from langchain_core.output_parsers import StrOutputParser
from app.config.llm import  llm
from app.prompts.keyword_prompt import keyword_prompt

keyword_chain = keyword_prompt | llm | StrOutputParser()