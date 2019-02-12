import string
import random
import json
from flask import request, jsonify
from ..store import store


def add_user ():
    user_data = json.loads(request.data)
    users = store.add_user(user_data)
    token = generate_token()
    tokens = store.add_token(token, user_data)
    return jsonify({ token: token })



def generate_token():
    chars = string.ascii_letters + string.digits

    token = ""
    for i in range(10):
        rand_index = random.randint(0, 61)
        token += chars[rand_index]
    return token
