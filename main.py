from fastapi import FastAPI
import ollama

app = FastAPI()

# routes
@app.post("/generate")
def generate(prompt: str):
    response = ollama.chat(model="llama3.1:8b", messages=[{"role":"user", "content":prompt}])
    return {"response":response["message"]["content"]}