from models.base_model import db

from models.users import User


db.create_tables([User])