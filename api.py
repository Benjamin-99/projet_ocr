from fastapi import FastAPI

import unicorn

app = FastAPI()



@app.get("/")
async def hello_world():
 return {"hello": "world"}

if __name__== "__main__":
    unicorn.run(app, host="127.0.0.1", port=8000)