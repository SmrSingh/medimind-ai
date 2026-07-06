from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.chat import router as chat_router
from backend.app.api.report import router as report_router
from backend.app.api.report_chat import router as report_chat_router

app = FastAPI(
    title="MediMind AI",
    description="AI-powered Clinical Decision Support Platform",
    version="0.1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    chat_router,
    prefix="/api",
    tags=["Medical Chat"]
)

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