import os


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_SECRET_KEY =  os.environ.get("SECRET_KEY")
    
    @property # creates getter and setter methods for the property
    def SQLALCHEMY_DATABASE_URI(self):
        db_url = os.environ.get("DATABASE_URL")

        if not db_url:
            raise ValueError("DATABASE_URL is not set")

        return db_url
  
    
# three environments: 
class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True


environment = os.environ.get("FLASK_DEBUG")


if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()
