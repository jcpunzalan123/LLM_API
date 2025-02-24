from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

API_KEYS_CREDITS = {os.getenv("API_KEY"): 10}

def verify_api_key(x_api_key:str=Header(None)):
    credits = API_KEYS_CREDITS.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code=401, detail="Invalid API Key, or no credits")
    return x_api_key

# routes
@app.post("/generate")
def generate(prompt: str, x_api_key: str=Depends(verify_api_key)):
    API_KEYS_CREDITS[x_api_key] -= 1
    response = ollama.chat(model="llama3.1:8b", messages=[{"role":"user", "content":prompt}])
    return {"response":response["message"]["content"]}