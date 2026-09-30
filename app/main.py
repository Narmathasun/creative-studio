import os
from fastapi import FastAPI

app = FastAPI(title="Multi-Agent Creative Studio")


@app.get("/health")
def health():
    return {"status": "ok", "llm_key_configured": bool(os.getenv("ANTHROPIC_API_KEY"))}

@app.get("/")
def root():
    return {"message": "Creative Studio is running. Try /health or /docs"}
