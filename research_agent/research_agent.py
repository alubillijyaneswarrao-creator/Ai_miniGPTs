from tools.web_search import web_search
from llm import ask_llm


def research_agent(topic):

    search_results = web_search(topic)

    prompt = f"""
You are a research agent.

Topic:
{topic}

Search Results:
{search_results}

Generate a structured research report.
"""

    return ask_llm(prompt)