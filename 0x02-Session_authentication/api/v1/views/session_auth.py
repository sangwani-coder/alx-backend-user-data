#!/usr/bin/env python3
""" handles all routes for Session auth"""
from flask import requests. jsonify
from models.user import User

@app.app_views.route('/auth_session/login',
                     methods=['POST'], strict_slashes=False)
def auth_session() -> str:
    """ session auth"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or email is None:
        return jsonify({'error': "email missing"}), 400

    if not password or password is None:
        return jsonify({'error': "wrong password"}), 400

    # check user in DB
    try:
        users = User.search({"email": user_email})
        if user is None:
            return jsonify({'error': "no user found for this email"}), 404
        if user.is_valid_password(password):
            from os import getenv
            SESSION_NAME = getenv('SESSION_NAME')
            from api.v1.app import auth
            sID = auth.create_session(email)
            user.set_cookie(SESSION_NAME, sID)
            return user.to_json()
        else:
            return jsonify({'error': "wrong pssword"}), 401
