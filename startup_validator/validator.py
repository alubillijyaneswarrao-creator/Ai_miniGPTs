from llm import ask_llm

def validate_startup(idea):

    prompt = f"""
You are a startup analyst.

Evaluate this startup idea:

{idea}

Provide:

1. Market demand
2. Competitors
3. Feasibility
4. Monetization strategy
5. Score out of 10
"""

    return ask_llm(prompt)