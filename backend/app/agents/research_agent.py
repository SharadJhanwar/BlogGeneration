import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from app.tools import ALL_TOOLS

load_dotenv()

# 1. Initialize the LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# 2. Define System Prompt
system_prompt = """You are a professional Research Assistant.
    
CRITICAL RULES:
1. RELEVANCE: Your research MUST be strictly focused on the provided topic. 
2. NOISE REDUCTION: Ignore general news, politics, or unrelated events that do not directly pertain to the core topic.
3. STRUCTURE: Return a concise, factual summary of your findings related ONLY to the topic.
4. MANDATORY SEARCH: If the user asks for 'Trends', 'Recent', or 'Latest' information, YOU MUST use the 'web_search' tool.

Current Date: 2025-12-30
"""

# 3. Create the Agent using the available create_agent function
agent_executor = create_agent(
    "gpt-4o-mini",
    tools=ALL_TOOLS,
    system_prompt=system_prompt
)
