from sanic_openapi import doc

class User:
    id = doc.Integer("The id of user.")
    username = doc.String("The name of user.")
    password = doc.String("The password of user.")

class UserBody:
    username = doc.String("The name of user.")
    password = doc.String("The password of user.")

class UserOne:
    data = doc.Object(User)

class UserList:
    data = doc.List(User)