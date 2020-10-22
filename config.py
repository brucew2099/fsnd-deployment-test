import os


class Config(object):
    USER = os.environ.get('postgressql.user')
    PASSWD = os.environ.get('postgressql.passwd')
    HOST = os.environ.get('postgressql.host')
    PORT = int(os.environ.get('postgressql.port', '5432'))
    DB = os.environ.get('postgressql.db')
    DBTEST = os.environ.get('postgressql.db_test')


class DevelopmentConfig(Config):
    DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
                        Config.USER, Config.PASSWD, Config.HOST,
                        Config.PORT, Config.DB)
    TEST_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(
                        Config.USER, Config.PASSWD, Config.HOST,
                        Config.PORT, Config.DBTEST)
