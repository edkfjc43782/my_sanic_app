from peewee import CharField, AutoField

from models.base_model import BaseModel


class User(BaseModel):

    id = AutoField()
    username = CharField(null=False, unique=True)
    password = CharField(null=False)

    @classmethod
    def create_user(cls, username, password):
        if not username or not password:
            raise ValueError
        user = cls.create(username=username, password=password)
        return user

    @classmethod
    def find_all(cls):
        users = cls.select()
        return users
    
    @classmethod
    def find_by_user_id(cls, user_id):
        user = cls.get_or_none(cls.id == user_id)
        return user

    @classmethod
    def update_by_id(cls, user_id, update_data):
        query = cls.update(**update_data).where(cls.id == user_id)
        query.execute()
        user = cls.get_or_none(cls.id == user_id)
        return user
    
    @classmethod
    def delete_by_id(cls, user_id):
        query = cls.delete().where(cls.id == user_id)
        query.execute()