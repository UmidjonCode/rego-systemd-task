from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI(title="Rego Cloud Intern Backend", version="1.0.0")

@app.get("/")
def home():
    return {"service": "rego-intern-api", "message": "Hello from FastAPI"}

@app.get("/health")
def health():
    return {"status": "ok", "timestamp": datetime.now(timezone.utc).isoformat()}

@app.get("/info")
def info():
    return {"application": "Rego Cloud Intern Backend", "runtime": "FastAPI"}
