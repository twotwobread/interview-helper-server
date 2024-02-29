from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def check_health():
    return {"status": 200, "description": "Server running"}
