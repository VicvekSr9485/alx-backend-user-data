#!/usr/bin/env python3
"""
Main file
"""

import requests


def register_user(email: str, password: str) -> None:
    """ test registration """
    url = "http://127.0.0.1:5000/users"
    payload = {"email": email, "password": password}
    response = requests.post(url, json=payload)
    assert response.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """ test login wrong password """
    url = "http://127.0.0.1:5000/sessions"
    payload = {"email": email, "password": password}
    response = requests.post(url, json=payload)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """ test login """
    url = "http://127.0.0.1:5000/sessions"
    payload = {"email": email, "password": password}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    return response.json()["session_id"]


def profile_unlogged() -> None:
    """ test profile_unlogged """
    url = "http://127.0.0.1:5000/profile"
    response = requests.get(url)
    assert response.status_code == 401


def profile_logged(session_id: str) -> None:
    """ test profile logged """
    url = "http://127.0.0.1:5000/profile"
    headers = {"Authorization": session_id}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200


def log_out(session_id: str) -> None:
    """ test logout """
    url = "http://127.0.0.1:5000/sessions"
    headers = {"Authorization": session_id}
    response = requests.post(url, headers=headers)
    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """ test reset password token """
    url = "http://127.0.0.1:5000/reset_password"
    payload = {"email": email}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    return response.json()["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ test update_password """
    url = "http://127.0.0.1:5000/reset_password"
    payload = {"email": email, "reset_token": reset_token,
               "new_password": new_password}
    response = requests.post(url, json=payload)
    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
