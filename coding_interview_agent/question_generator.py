from llm import ask_llm

def generate_question(topic, difficulty):

    prompt = f"""
Generate a coding interview question.

Topic: {topic}
Difficulty: {difficulty}

Include:

Problem Statement
Example
Constraints
Expected Approach
"""

    return ask_llm(prompt)