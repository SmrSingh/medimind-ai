from fastapi import FastAPI
from backend.app.api.chat import router as chat_router
from backend.app.api.report import router as report_router
from backend.app.api.report_chat import router as report_chat_router
app = FastAPI(
    title="MediMind AI",
    description="AI-powered Clinical Decision Support Platform",
    version="0.1.0"
)
app.include_router(
    chat_router,
    prefix="/api",
    tags=["Medical Chat"]
)

@app.get("/")
def root():
    return {
        "message": "Welcome to MediMind AI 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(
    report_router,
    prefix="/api",
    tags=["Report Analysis"]
)

app.include_router(
    report_chat_router,
    prefix="/api",
    tags=["Report Chat"]
)