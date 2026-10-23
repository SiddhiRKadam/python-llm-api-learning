#DAY 4 & 6

#FASTAPI - creat routes andAPIS (car)
#UVICORN - runs the FASTAPI application (engine) both together are necessary
#route is important as it is simple URL endpoint.
#Task 2
from fastapi import FastAPI #importing the fastapi class

app = FastAPI() #creates you web application

@app.get("/") # Create Route : whensomeone visits i.e / run the below function
def home(): #defininf a function
    return {"message": "Hello FastAPI"}

#Task 3
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message":"hello FastAPI"}
@app.get("/students")
def students():
    return ["Aadi","Mansi","Apeksha","Siddharth","Nirmit","Umang","Ankush","Esha","Hardik"]

#Task 4
from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"message":"hello FastAPI"}
@app.get("/students")
def students():
    return ["Aadi","Mansi","Apeksha","Siddharth","Nirmit","Umang","Ankush","Esha","Hardik"]
@app.get("/students/rahul")
def task():
    return {"student": "rahul"}

#Task 5 done




#DAY 6

#Task 1
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
@app.get("/ask")
def ask():
    return {"message": "Route working"}


#Task 2
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
@app.get("/ask")
def ask(query:str): #user types in browser
    return {"query": query}

#Task 3
from fastapi import FastAPI
from llm import ask_llm

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


@app.get("/ask")
def ask(query: str):

    answer = ask_llm(query)

    return {
        "answer": answer
    }

