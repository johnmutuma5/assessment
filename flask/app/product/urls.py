from flask import Blueprint
from .views import add_product

product = Blueprint('products', __name__)

product.add_url_rule('', view_func=add_product, methods=['POST'])
