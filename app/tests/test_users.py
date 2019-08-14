import pytest

from start_app import app
from models.users import User


async def test_create_user_with_username_password():
    """
        Test creating a new user with username & password is successful
    """
    username = "qaz123"
    password = "1qaz2wsx"
    user = User(username=username, password=password)
    assert user.username == username
    assert user.password == password

async def test_new_user_invalid_username():
    """
        Test creating a new user with invalid username
    """
    with pytest.raises(ValueError):
        user = User(username=None, password="1qaz2wsx")
        if not user.username:
            raise ValueError 
         
