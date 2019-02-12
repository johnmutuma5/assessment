import os
import string
import json
import jwt
from flask import request, jsonify
from ..store import store
from ..shared.exceptions import AuthenticationError
from .. import app
from ..shared.middleware import admin_only, require_token

APP_SECRET = app.config['APP_SECRET']

class UserController:

    @staticmethod
    @require_token
    @admin_only
    def add_user ():
        user_data = json.loads(request.data)
        user = store.add_user(user_data)
        return jsonify({ 'ok': True, 'user': user})

    @staticmethod
    def authenticate ():
        login_credentials = json.loads(request.data)
        try:
            user = store.find_user(login_credentials)
        except AuthenticationError as e:
            return jsonify({ 'ok': False,'message': e.message }), 403
        # generate JWT token
        payload = { 'username': user['username'], 'role': user['role'] }
        token = jwt.encode(payload, APP_SECRET, algorithm='HS256')
        return jsonify({ 'token': token.decode('utf8') })
