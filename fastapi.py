"""
FastAPI Tutorial - Complete with Code Examples and Expected Outputs

Following the course material by Wahid Hamdi
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Section 1: Why Use FastAPI?
"""
Why Use FastAPI?
- Easy to learn
- Fast development
- High performance (async by default)
"""

# Section 2: Installation and Setup
"""
Install and Get Started with FastAPI:
1. pip install fastapi uvicorn
2. Create main.py with basic FastAPI app
"""

# Basic FastAPI app
print("\n=== BASIC FASTAPI APP ===")
print("""
Code:
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

Run with: uvicorn main:app --reload
Expected Output: Visit http://127.0.0.1:8000
Should return: {"Hello":"World"}
""")

# Section 3: GET and POST Routes
print("\n=== GET AND POST ROUTES ===")

# Todo list application setup
items = []

print("""
Code:
items = []

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return item

Test with:
curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'
Expected Output: "apple"
""")

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return item

print("""
Code:
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items[item_id]

Test with:
curl -X GET http://127.0.0.1:8000/items/0
Expected Output: "apple"
""")

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items[item_id]

# Section 4: Handling HTTP Errors
print("\n=== HANDLING HTTP ERRORS ===")
print("""
Code:
from fastapi import HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    return items[item_id]

Test with:
curl -X GET http://127.0.0.1:8000/items/7
Expected Output: {"detail":"Item 7 not found"}
""")

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    return items[item_id]

# Section 5: JSON Request and Path Parameters
print("\n=== JSON REQUEST AND PATH PARAMETERS ===")
print("""
Code:
@app.get("/items/")
def list_items(limit: int = 10):
    return items[0:limit]

Test with:
curl -X GET 'http://127.0.0.1:8000/items?limit=3'
Expected Output: ["apple"] (or your items)
""")

@app.get("/items/")
def list_items(limit: int = 10):
    return items[0:limit]

# Section 6: Pydantic Models
print("\n=== PYDANTIC MODELS ===")
print("""
Code:
from pydantic import BaseModel

class Item(BaseModel):
    text: str
    is_done: bool = False

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item

Test with:
curl -X POST -H "Content-Type: application/json" -d '{"text":"apple"}' 'http://127.0.0.1:8000/items'
Expected Output: {"text":"apple","is_done":false}
""")

class Item(BaseModel):
    text: str
    is_done: bool = False

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item

# Section 7: Response Models
print("\n=== RESPONSE MODELS ===")
print("""
Code:
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    return items[item_id]

Test with:
curl -X GET 'http://127.0.0.1:8000/items'
Expected Output: [{"text":"apple","is_done":false}]
""")

@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    return items[item_id]

# Section 8: Interactive Documentation
print("\n=== INTERACTIVE DOCUMENTATION ===")
print("""
FastAPI automatically generates interactive documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
""")

# Section 9: FastAPI vs Flask vs Django
print("\n=== FASTAPI VS FLASK VS DJANGO ===")
print("""
FastAPI is:
- Async by default
- Easier to use
- Better performance

Flask:
- More complex
- Not async by default

Django:
- Heavyweight framework
- More batteries included
""")

if __name__ == "__main__":
    print("\n=== FASTAPI TUTORIAL ===")
    print("To run this FastAPI application:")
    print("1. Save this file as main.py")
    print("2. Install dependencies: pip install fastapi uvicorn")
    print("3. Run: uvicorn main:app --reload")
    print("4. Visit http://127.0.0.1:8000/docs for interactive API documentation")
    print("\n=== END OF TUTORIAL ===")