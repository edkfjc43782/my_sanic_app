import pytest

from models.users import User
from models.create_db import create_tables


create_tables()


async def test_create_user_with_username_password():
    """
        Test creating a new user with username & password is successful
    """
    username = "qaz123"
    password = "1qaz2wsx"
    user = User.create_user(username=username, password=password)
    assert user.username == username
    assert user.password == password


async def test_create_valid_new_user():
    """
        Test creating a new user with invalid value
    """
    with pytest.raises(ValueError):
        User.create_user(username=None, password="1qaz2wsx")


async def test_find_user_by_username():
    """
    Test find a user by username
    """
    username = "qaz123"
    user = User.find_by_username(username)
    if user:
        assert user.username == username
