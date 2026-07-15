from fastapi import FastAPI
from core.openjarvis.agent import JarvisAgent

app = FastAPI()
agent = JarvisAgent()


@app.post("/chat")
def chat(message: str):
    response = agent.ask(message)
    return {
        "response": response
    }