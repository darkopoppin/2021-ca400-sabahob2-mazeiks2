from app import db


def assignCategories(data):
    userId = data['params'][-1]
    db.reference('users').child(userId).set(data['params'][0])
    return 'assigned'
