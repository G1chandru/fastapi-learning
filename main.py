from fastapi import FastAPI
from models import product
app = FastAPI()
@app.get("/")
def greet():
    return "Welcome to The Jungle"
products = [
    product(id=1, name="phone", description="iphone", price=999.9, quantity=1),
    product(id=2, name="laptop", description="hp", price=9999.9, quantity=1),
    product(id=13, name="pencil", description="natraj", price=9.9, quantity=1),
    product(id=44, name="pen", description="XO", price=1.9, quantity=1),
]
@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def ger_product_by_id(id : int):
    for product in products:
        if product.id == id:
            return product
    return "product not found"


@app.post("/product")
def add_product(new_product: product):
    products.append(new_product)
    return new_product
@app.put("/product")
def update_product(id: int,product:product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product Added Successfully"
    return "no product found"
@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product is deleted successfully"
    return "product is not found"