from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Hello FastAPI!"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello FastAPI!"}

@app.get("/info")
def get_info():
    return {"name": "HelloFastAPI!",
            "version": "1.0",
            "description": "My first FastAPI application"
            }

@app.get("/items")
def get_items():
    return [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Keyboard"},
        {"id": 3, "name": "Mouse"}
    ]

#path parameter endpoint
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {
        "item_id": item_id,
        "name": f"Item {item_id}"
    }