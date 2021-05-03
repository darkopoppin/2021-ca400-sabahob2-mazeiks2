from os import environ

REDIS_PASS = environ.get('REDIS_PASS')
if environ.get('FLASK_ENV') == 'development':
    REDIS_HOST = 'localhost'
    REDIS_PORT = '5005'
else:
    REDIS_HOST = 'redis-server'
    REDIS_PORT = '6379'

if environ.get('FLASK_ENV') == 'development':
    RECOMM_HOST = '127.0.0.1'
else:
    RECOMM_HOST = 'recommender'

if environ.get('FLASK_ENV') == 'development':
    PLANNER_HOST = '127.0.0.1'
else:
    PLANNER_HOST = 'planner'
YELP_API = environ.get('YELP_API')
