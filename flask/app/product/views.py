import json
from flask import jsonify, request
from ..store import store

def add_product():
    product_data = json.loads(request.data)
    products = store.add_product(product_data)
    return jsonify(products)
