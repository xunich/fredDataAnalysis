from fastapi import FastAPI

app = FastAPI()  # This creates a FastAPI app instance.

# Define a route at the root URL "/"
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}  # Returns JSON when visited.

# Define another route with a parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
