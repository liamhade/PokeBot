from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
	return {"message": "Hello world!"}

@app.get("/say")
def read_say(words: str):
	return {"message": {words}}