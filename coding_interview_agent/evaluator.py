from llm import ask_llm

def evaluate_solution(question, solution):

    prompt = f"""
Evaluate this coding solution.

Question:
{question}

Solution:
{solution}

Provide:

1. Correctness
2. Time Complexity
3. Improvements
4. Score out of 10
"""

    return ask_llm(prompt)