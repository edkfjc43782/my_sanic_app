from peewee import CharField

from models.base_model import BaseModel, db


class User(BaseModel):
    username = CharField()
    password = CharField()

