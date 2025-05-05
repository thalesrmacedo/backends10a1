from database import products_collection

def add_product(name, price, stock):
    product = {"name": name, "price": price, "stock": stock}
    products_collection.insert_one(product)
    return f"Produto '{name}' adicionado!"

def get_all_products():
    return list(products_collection.find({}, {"_id": 0}))

def get_product_by_name(name):
    return products_collection.find_one({"name": name}, {"_id": 0})

def update_product(name, updated_fields):
    products_collection.update_one({"name": name}, {"$set": updated_fields})
    return f"Produto '{name}' atualizado!"

def delete_product(name):
    products_collection.delete_one({"name": name})
    return f"Produto '{name}' removido!"
