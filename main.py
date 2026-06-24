from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def root():
    return "Hello World"

products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A gaming laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=5, name="Table", description="A wooden table", price=199.99, quantity=20),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return "Product added successfully"

@app.put("/product/{id}")
def update_product(id: int, product: Product):
    for i, p in enumerate(products):
        if p.id == id:
            products[i] = product
            return f"Product with id {id} updated successfully"
    return {"error": "Product not found"}   

@app.delete("/product/{id}")
def delete_product(id: int):
    for i, p in enumerate(products):
        if p.id == id:
            products.pop(i)
            return f"Product with id {id} deleted successfully"
    return {"error": "Product not found"}
