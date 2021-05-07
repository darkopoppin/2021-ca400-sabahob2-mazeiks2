from service import db

from planner.plan import Plan


class User(object):

    def __init__(
            self, user_id, age, gender, location,
            liked_categories, visited=None
    ):
        self.user_id = user_id
        self.age = int(age)
        self.gender = gender
        self.location = location
        self.liked_categories = liked_categories
        self.visited = visited

    @staticmethod
    def from_dict(data, user_id=None):
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

    def save(self):
        db.collection('users').document(self.user_id).set(self.to_dict())

    def init_plan(self, activities, coordinates, start_time, end_time):
        self.plan = Plan(
            activities, coordinates, start_time, end_time,
            self.liked_categories
        )

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
