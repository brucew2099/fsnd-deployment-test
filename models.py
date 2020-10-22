import os

from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy

database_path = os.environ.get('DATABASE_PATH')

if database_path is None:
    database_path = "postgresql://{}:{}@{}:{}/{}".format(
                        os.environ.get('USER'),
                        os.environ.get('PASSWD'),
                        os.environ.get('HOST'),
                        os.environ.get('PORT'),
                        os.environ.get('DB'))

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''


class Person(db.Model):
    __tablename__ = 'People'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    catchphrase = Column(String)

    def __init__(self, name, catchphrase=""):
        self.name = name
        self.catchphrase = catchphrase

    def format(self):
        return {
          'id': self.id,
          'name': self.name,
          'catchphrase': self.catchphrase
        }
