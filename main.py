from fastapi import FastAPI
import uvicorn
import os
import openai
from dotenv import load_dotenv

# load_dotenv()  # blank if .env file in same directory as script
# # load_dotenv('<path to file>.env') to point to another location
key = os.getenv("OPENAI_API_KEY")

openai.api_key = key

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "IDS706 Project4"}

@app.get("/chat/{message}")
async def chat(message: str):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=message,
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
    )
    print(response)
    return response

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
    