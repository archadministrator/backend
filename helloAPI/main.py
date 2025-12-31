from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def readRoot():
    return {"message":"Hello World"}

@app.get("/hi/{name}")
def greeting(name: str):
    return {"message": f"Hello {name}"}
