from langchain_core.output_parsers import StrOutputParser
from app.prompts.image_topic_prompt import image_topic_prompt
from app.config.llm import llm

image_topic_chain = image_topic_prompt | llm | StrOutputParser()
