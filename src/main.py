from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Platform",
    description="Enterprise RAG and Agentic AI Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Enterprise AI Platform is running",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }