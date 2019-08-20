import pytest
from pathlib import Path

from start_app import app
from models.users import User
from models.create_db import create_tables


create_tables()


# async def test_createUser_usernamePassword_userinfo():

#     # arrange
#     expected_username = "tgbyhn45"
#     expected_password = "6754345"

#     # act
#     user = User.create_user(username=expected_username, password=expected_password)

#     # assert
#     assert user.username == expected_username
#     assert user.password == expected_password


async def test_createUser_noneUsernamePassword_raiseValueError():

    # arrange
    expected_username = None
    expected_password = None

    # act & assert
    with pytest.raises(ValueError):
        User.create_user(username=expected_username, password=expected_password)


def test_get_users():
    url = str(Path("/").joinpath("users"))
    request, response = app.test_client.get(url)
    assert response.status == 200


def test_get_user(user_id):
    url = str(Path("/").joinpath("users", user_id))
    request, response = app.test_client.get(url)
    assert response.status == 200


def test_create_user(new_user):
    url = str(Path("/").joinpath("users"))
    data = {"username": new_user["username"], "password": new_user["password"]}
    request, response = app.test_client.post(url, json=data)
    assert response.status == 200


def test_update_user(user_id):
    url = str(Path("/").joinpath("users", user_id))
    data = {"username": "updateusername", "password": "updatepassword"}
    request, response = app.test_client.put(url, json=data)
    assert response.status == 200


def test_delete_user(user_delete_id):
    url = str(Path("/").joinpath("users", user_delete_id))
    request, response = app.test_client.delete(url)
    assert response.status == 200