from research_agent.research_agent import research_agent
from startup_validator.validator import validate_startup
from coding_interview_agent.question_generator import generate_question
from memory.memory_store import save_to_memory


def manager_agent(query):

    q = query.lower()

    if "startup" in q or "idea" in q:
        result = validate_startup(query)

    elif "coding" in q or "question" in q:
        result = generate_question("Algorithms", "Medium")

    else:
        result = research_agent(query)

    save_to_memory(query, result)

    return result