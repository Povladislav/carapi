import pytest

from customer.models import User


@pytest.fixture
def user():
    user = User.objects.create_user(
        username="harryPotter",
        email="nu2@gmail.com",
        password="user2",
    )

    return user
