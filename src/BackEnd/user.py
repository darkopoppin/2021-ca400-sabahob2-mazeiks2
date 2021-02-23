import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

if (not len(firebase_admin._apps)):
    cred = credentials.Certificate('./confidential.json')
    default_app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://citecy-default-rtdb.europe-west1.firebasedatabase.app/'})

datab = db


def assignCategories(data):
    userId = data['params'][-1]
    datab.reference('users').child(userId).set(data['params'][0])
    return 'assigned'