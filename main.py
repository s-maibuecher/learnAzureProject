from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    count = 1
    return {"message": f"Endpoint was called {count} times"}
