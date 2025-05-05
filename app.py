from flask import Flask, request, jsonify
from products import add_product, get_all_products, get_product_by_name, update_product, delete_product

app = Flask(__name__)

@app.route("/products", methods=["POST"])
def add_product_route():
    data = request.json
    return jsonify(add_product(data["name"], data["price"], data["stock"]))

@app.route("/products", methods=["GET"])
def get_all_products_route():
    return jsonify(get_all_products())

@app.route("/products/<name>", methods=["GET"])
def get_product_route(name):
    return jsonify(get_product_by_name(name))

@app.route("/products/<name>", methods=["PUT"])
def update_product_route(name):
    data = request.json
    return jsonify(update_product(name, data))

@app.route("/products/<name>", methods=["DELETE"])
def delete_product_route(name):
    return jsonify(delete_product(name))

if __name__ == "__main__":
    app.run(debug=True)
