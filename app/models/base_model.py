from peewee import SqliteDatabase, Model


db = SqliteDatabase('mysanicapp.db')

class BaseModel(Model):
    class Meta:
        database = db