import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def getName():
    return {"Anurag":"yolodolosolo"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")