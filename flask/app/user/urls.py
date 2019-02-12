from flask import Blueprint
from .views import add_user

user = Blueprint('user', __name__)

user.add_url_rule('', view_func=add_user, methods=['POST'])
