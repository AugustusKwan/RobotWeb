import os

with open('E:\\Robot\\JSON\PW.JSON','r') as json_f:
    json_dict = json.load(json_f)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'



class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Forever98@localhost:3306/demo"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'docker': DockerConfig,

    'default': DevelopmentConfig
}
