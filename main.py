from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def welcome():
    return { 
        "message ": "hello world"
    }

# i stop at 5 min at 05 vid