from start_app import app

from models.users import User


async def test_create_user_with_username_password():
    """
        Create a new user with username and password
    """
    username = "qaz123"
    password = "1qaz2wsx"
    user = User(username=username, password=password)
    assert user.username == username
    assert user.password == password
