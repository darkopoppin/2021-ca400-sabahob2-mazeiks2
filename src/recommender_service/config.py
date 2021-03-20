class Config(object):
    DEBUG = False
    TESTING = False

    FIREBASE_CONFIG = {
        "apiKey": "AIzaSyBO0wRTtvrYhE6V6ublQmb7bNmQf7NVEsU",
        "authDomain": "citecy.firebaseapp.com",
        "databaseURL": "https://citecy-default-rtdb.europe-west1.firebasedatabase.app",
        "storageBucket": "citecy.appspot.com"
    }

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True