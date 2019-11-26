import os

class Config:
    SECRET_KEY ='dominic'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:dominic@localhost/pitches'
    



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}