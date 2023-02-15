#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def welcome() -> str:
    """ app route """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_users() -> str:
    """ register users """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        if user:
            return jsonify({
                "email": user.email,
                "message": "user created"
            })
    except ValueError:
        return jsonify({
            "message": "email already registered"
        }), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """  Log in """
    email = request.form.get("email")
    password = request.form.get("password")

    valid_credentials = AUTH.valid_login(email, password)
    if not valid_credentials:
        abort(401)

    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """ Log out """
    cookie = request.cookies.get("session_id", None)
    user = AUTH.get_user_from_session_id(cookie)
    if cookie is None or user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> str:
    """ User profile function """
    cookie =  request.cookies.get("session_id", None)
    user = AUTH.get_user_from_session_id(cookie)
    if user is None or cookie is None:
        abort(403)
    return jsonify({"email": user.email}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
