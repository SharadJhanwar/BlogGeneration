from langchain_core.output_parsers import StrOutputParser
from app.prompts.section_prompt import section_prompt
from app.config.llm import  llm

section_chain = section_prompt | llm | StrOutputParser()
