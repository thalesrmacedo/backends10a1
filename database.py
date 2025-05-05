from pymongo import MongoClient

# Conectar ao MongoDB (por padrão, ele roda na porta 27017)
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce_db"]  # Nome do banco de dados
products_collection = db["products"]  # Coleção para armazenar os produtos
