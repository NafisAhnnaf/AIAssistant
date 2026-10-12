from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def welcome():
	return {"message": "Hello Wolrd!"}
