from os import environ

REDIS_PASS = environ.get('REDIS')
if environ.get('FLASK_ENV') == 'development':
    REDIS_HOST = 'localhost'
    REDIS_PORT = '5005'
    HOST = '127.0.0.1'

# add for testing and production

if environ.get('FLASK_ENV') == 'development':
    RECOMM_HOST = '127.0.0.1'
else:
    RECOMM_HOST = 'recommender'
