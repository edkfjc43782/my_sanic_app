import pytest

from models.users import User


@pytest.fixture(scope="session")
def user_id():
    return "1"


@pytest.fixture(scope="session")
def new_user():
    user = {"username": "testusername", "password": "testpassword"}
    yield user
    User.delete_by_username("testusername")


@pytest.fixture(scope="session")
def user_delete_id():
    user = User.create_user("deleteusername", "deletepassword")
    return str(user.id)