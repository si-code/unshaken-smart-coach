from fastapi import FastAPI

app = FastAPI(
    title="UNShaken Smart Coach API",
    description="Backend API for the UNShaken Smart Coach application",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to UNShaken Smart Coach API"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }