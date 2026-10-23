from fastapi import FastAPI
from llm import ask_llm
from datetime import datetime

app = FastAPI()

question_history = []


@app.get("/")
def home():
    return {
        "message": "AI Study Assistant"
    }


@app.get("/ask")
def ask(query: str):

    question_history.append(query)

    answer = ask_llm(query)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    count = 0

    for question in question_history:
        count += 1

    with open("chat_history.txt", "a") as file:

        file.write(f"Time: {timestamp}\n")
        file.write(f"Question: {query}\n")
        file.write(f"Answer: {answer}\n")
        file.write("-" * 50 + "\n")

    return {
        "question": query,
        "answer": answer,
        "timestamp": timestamp,
        "total_questions": count
    }


@app.get("/history")
def history():

    return {
        "questions": question_history
    }