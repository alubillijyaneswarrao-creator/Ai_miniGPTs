from fastapi import FastAPI
from research_agent.research_agent import research_agent
from startup_validator.validator import validate_startup
from coding_interview_agent.question_generator import generate_question
from coding_interview_agent.evaluator import evaluate_solution

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Agents Running"}

@app.get("/research")
def research(topic: str):
    return {"result": research_agent(topic)}

@app.get("/startup")
def startup(idea: str):
    return {"analysis": validate_startup(idea)}

@app.get("/generate-question")
def question(topic: str, difficulty: str):
    return {"question": generate_question(topic, difficulty)}

@app.post("/evaluate")
def evaluate(question: str, solution: str):
    return {"evaluation": evaluate_solution(question, solution)}