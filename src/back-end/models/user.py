from main_service import db
from firebase_admin import firestore


class User(object):

    def __init__(
            self, user_id, age, gender, location,
            liked_categories=None, visited=None
    ):
        self.user_id = user_id
        self.age = int(age)
        self.gender = gender
        self.location = location

        if liked_categories is None:
            liked_categories = []
        self.liked_categories = liked_categories

        if visited is None:
            visited = {}
        self.visited = visited

    def updateCategories(self, categories):
        self.liked_categories = categories

    @staticmethod
    def from_dict(user_id, data):
        user = User(
            user_id=user_id,
            age=int(data['age']),
            gender=data['gender'],
            location=data['location'],
            liked_categories=data['liked_categories'],
            visited=data['visited']
        )
        return user

    def to_dict(self):
        user = {}
        user.update({'age': self.age})
        user.update({'gender': self.gender})
        user.update({'location': self.location})
        user.update({'liked_categories': self.liked_categories})
        user.update({'visited': self.visited})
        return user

    def save(self, categories=False):
        if categories:
            user = db.collection('users').document(self.user_id)
            user.update(
                {'liked_categories': firestore.ArrayUnion(
                    self.liked_categories
                )}
            )
        else:
            db.collection('users').document(self.user_id).set(self.to_dict())

    def __repr__(self):
        return (
            f'User(\
                user_id={self.user_id}\
                age={self.age}\
                gender={self.gender}\
                location={self.location}\
                liked_categories={self.liked_categories}\
                visited{self.visited}\
            )'
        )
