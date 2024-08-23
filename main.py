from fastapi import FastAPI
import uvicorn
from models import Product
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.get("/products")
def get_products():
    try:
        query = Product.select().order_by(Product.product_id).dicts()
        return {'products':list(query)}
    except:
        return {'error': "no records in table"}

@app.get("/products/{product_id}")
def get_product(product_id : int):
    try:
        query = Product.get_by_id(product_id)
        return {'product': query.__data__}
    except:
        return {'error': "item does not exist"}

@app.get("/recommendation/{product_id}")
def get_recommendation(product_id : int):
    try:
        query = Product.select().order_by(Product.product_id).dicts()
        return {'recommendation': random.sample(list(query), 2)}
    except:
        return {'status': "error"}

if __name__ == "__main__":
    uvicorn.run(app)
