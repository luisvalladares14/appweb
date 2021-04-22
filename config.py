class Config:
    SECRET_KEY = '142007'
    pass;

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_DB = 'tienda'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
