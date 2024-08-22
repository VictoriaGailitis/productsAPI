from fastapi import FastAPI
import uvicorn
from models import Product

app = FastAPI()

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

if __name__ == "__main__":
    uvicorn.run(app)
