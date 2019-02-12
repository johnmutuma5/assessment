import json
from flask import jsonify, request
from ..store import store
from ..shared.middleware import admin_only, require_token

class ProductController:

    @staticmethod
    @require_token
    @admin_only
    def add_product ():
        product_data = json.loads(request.data)
        product = store.add_product(product_data)
        return jsonify({
            'product': product,
            'ok': True
        })

    def view_products ():
        products = store.get_all_products()
        return jsonify({
            'products': products,
            'ok': True
        })
