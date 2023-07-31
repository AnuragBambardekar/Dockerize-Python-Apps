import uvicorn
from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host="redis", port=6379)

@app.get("/")
def getName():
    return {"Anurag":"yolodolosolo"}

@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"number of hits": r.get("hits")}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")