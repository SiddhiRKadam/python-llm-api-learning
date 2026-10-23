#Day 3 & day 5 below
#Task 1 done:

#Task 2:
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url) # basically means, hey server, send me data!
#response contains status code,headers,actual data

# print(response)
#now for actual data print in JSON format!
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url) # basically means, hey server, send me data!
#response contains status code,headers,actual data

print(response.json())

#Task 3
import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()
for user in users:
    print(user['name'])

#task 4
import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users=response.json()
total_user=0
for user in users:
    total_user+=1
print("total_user=",total_user)

#Task 5
import requests
def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    posts = response.json()
    return posts
all_posts = fetch_posts()
print("Total Posts:", len(all_posts))






#DAY 5
#Task 1 and 2 loading the API KEY:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print("api_key is loaded successfully")

#Task 3 calling the LLM
# .env - load_dotenv() - os.getenv() - api_key variable

from dotenv import load_dotenv
import os
import google.generativeai as genai
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key) #tells google this is my API Key (authenticate)

model = genai.GenerativeModel("gemini-2.5-flash") #model = connection to gemini

response = model.generate_content(
    "Explain what is RAG in simple words"
) # same as day 3 for url which was api-stored data and here it is LLM-Generates new data
print(response.text)

#pip install -U google-genai (as google has deprecated the old SDK- software developement kit)
#SDK - It is a downloadable bundle that provides everything a developer needs to build apps for a specific platform, operating system, or hardware.


from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain what is RAG in simple words"
)

print(response.text)

#Task 4
from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
api_key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-2.5-flash")
response=model.generate_content(
    input("Ask me anything: ")
)
print(response.text)

#Task 5

from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

while True:

    question = input("Ask me anything: ")

    if question.lower() == "exit":
        print("Chatbot stopped.")
        break

    response = model.generate_content(question)

    print(response.text)


 

