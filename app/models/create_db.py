from models.base_model import db

from models.users import User
# from models.books import Book


def create_tables():
    with db:
        db.create_tables([User])
