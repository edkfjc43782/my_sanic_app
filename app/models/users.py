from peewee import CharField, AutoField

from models.base_model import BaseModel


class User(BaseModel):

    id = AutoField()
    username = CharField(null=False)
    password = CharField(null=False)

    @classmethod
    def create_user(cls, username, password):
        if not username or not password:
            raise ValueError
        user = cls.create(username=username, password=password)
        return user

    @classmethod
    def find_by_username(cls, username):
        user = cls.get_or_none(cls.username == username)
        return user
