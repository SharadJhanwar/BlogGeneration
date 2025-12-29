from langchain_core.output_parsers import StrOutputParser
from app.prompts.outline_prompt import outline_prompt
from app.config.llm import  llm

outline_chain = outline_prompt | llm | StrOutputParser()