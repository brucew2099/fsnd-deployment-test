import os

from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy

import dotenv
from os.path import abspath, dirname, join

database_path = os.environ.get('DATABASE_URL')

if database_path is None:
    project_dir = dirname(abspath(__file__))
    DOTENV_PATH = join(project_dir, '.env')
    
    database_path = "postgresql://{}:{}@{}:{}/{}".format(
                        dotenv.get_key(DOTENV_PATH, 'USER'),
                        dotenv.get_key(DOTENV_PATH, 'PASSWD'),
                        dotenv.get_key(DOTENV_PATH, 'HOST'),
                        dotenv.get_key(DOTENV_PATH, 'PORT'),
                        dotenv.get_key(DOTENV_PATH, 'DB'))

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
