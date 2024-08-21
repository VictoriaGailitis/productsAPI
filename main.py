from fastapi import FastAPI
import uvicorn
from models import Product

app = FastAPI()

@app.get("/products")
def get_products():
    query = Product.select().dicts()
    return {'products':list(query)}

if __name__ == "__main__":
    uvicorn.run(app)
