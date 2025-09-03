from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/favicon.ico")
async def favicon():
    return {"message": "Favicon not found"}