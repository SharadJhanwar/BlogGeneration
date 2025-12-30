from app.agents.research_agent import agent_executor
from app.chains.blog_agent.keyword_chain import keyword_chain
from app.chains.blog_agent.outline_chain import outline_chain
from app.chains.blog_agent.section_chain import section_chain
from app.chains.blog_agent.seo_chain import seo_chain


def blog2_pipeline(inputs: dict):
    print(f"We are starting pipeline execution for  : {inputs}")
    """
    Blog generation with agent-powered research + tools
    inputs:
    - title
    - tone
    - language
    """

    # Step 1: Agent builds factual context using tools
    research_prompt = f"""
    Research the topic thoroughly using tools if needed.

    Topic:
    {inputs['title']}

    Guidelines:
    - Use factual, verifiable information
    - Avoid speculation
    - Keep it concise and structured
    """

    research_result = agent_executor.invoke({
        "input": research_prompt
    })

    print(f"DEBUG: Research Result Type: {type(research_result)}")
    print(f"DEBUG: Research Result Keys: {research_result.keys()}")

    # Robust extraction of the final answer
    context = research_result.get("output")
    
    if not context and "messages" in research_result:
        # Many modern agents return the full message history. The last message is the answer.
        last_msg = research_result["messages"][-1]
        if hasattr(last_msg, "content"):
            context = last_msg.content
        elif isinstance(last_msg, dict) and "content" in last_msg:
            context = last_msg["content"]
        else:
            context = str(last_msg)
    
    if not context or context == "":
        context = "No research findings found."

    print(f"\n\n\nContext Extracted : {str(context)[:500]}...")

    # Step 2: Keyword extraction (grounded)
    keywords = keyword_chain.invoke({
        "title": inputs["title"],
        "context": context
    })

    # Step 3: Outline generation
    outline = outline_chain.invoke({
        "title": inputs["title"],
        "tone": inputs["tone"],
        "keywords": keywords,
        "context": context
    })

    # Step 4: Section writing
    content = section_chain.invoke({
        "outline": outline,
        "language": inputs["language"],
        "context": context
    })

    # Step 5: SEO polish
    final_content = seo_chain.invoke({
        "content": content,
        "keywords": keywords,
        "context": context
    })

    # Final response
    return {
        "keywords": keywords,
        "outline": outline,
        "content": final_content,
        "context": context
    }
