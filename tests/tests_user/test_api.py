import os

import jwt
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

client = APIClient()
pytestmark = pytest.mark.django_db

secret_key = "django-insecure-drp0!*s9xxjyt%f#@d+8ojy*)t^341iqnx6ry5$f_4p%7et_oj"


def test_user(user):
    client.force_authenticate(user)
    assert user.username == "harryPotter"


def test_register_user():
    payload = dict(
        username="harryPotter2", email="nu2@gmail.com", password="user232323"
    )
    response = client.post(reverse("register"), payload)
    assert response.status_code == 201
    assert response.data.get("username") == "harryPotter2"


def test_register_the_same_user(user):
    payload = dict(username="harryPotter", email="nu2@gmail.com", password="user2")
    response = client.post(reverse("register"), payload)

    assert response.status_code != 200


def test_login_user(user):
    credentials = dict(
        username="harryPotter",
        password="user2",
    )
    response = client.post(reverse("token_obtain_pair"), credentials)

    assert response.data.get("access") != None
    assert response.status_code == 200


def test_verify_email(user):
    client.force_authenticate(user)
    token = jwt.encode({"user_id": user.id}, secret_key, algorithm="HS256")
    payload = jwt.decode(token, secret_key, algorithms=["HS256"])
    response = client.get(reverse("email-verify"), {"token": token})
    assert payload["user_id"] == user.id
    assert response.data.get("email") == "Successfully activated!"
    assert response.status_code == 200
