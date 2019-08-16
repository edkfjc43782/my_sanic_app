from peewee import SqliteDatabase, Model


db = SqliteDatabase('/app/mysanicapp.db')


class BaseModel(Model):
    class Meta:
        database = db
