from models.users import User
from models.create_db import create_tables


create_tables()


async def test_find_all_users():
    """
        Test query all user data from db.
    """
    users = User.find_all()
    assert len(users) >= 0


# async def test_create_user_with_username_password():
#     """
#         Test creating a new user with username & password.
#         If username exists, raise ValueError.
#     """
#     username = "qaz123"
#     password = "1qaz2wsx"
#     user = User.create_user(username=username, password=password)
#     assert user.username == username
#     assert user.password == password
