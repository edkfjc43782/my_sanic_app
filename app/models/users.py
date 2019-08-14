from peewee import CharField, AutoField

from models.base_model import BaseModel, db


class User(BaseModel):

    id = AutoField() 
    username = CharField(null=False)
    password = CharField(null=False)



