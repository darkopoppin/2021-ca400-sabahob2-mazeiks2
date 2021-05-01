
class User(object):

    def __init__(self, age, gender, location, liked_categories=None, visited=None):
        self.age = age
        self.gender = gender
        self.location = location

        if liked_categories is None:
            liked_categories = []
        self.liked_categories = liked_categories

        if visited is None:
            visited = {}
        self.visited = visited

    def assignCategories(self, categories):
        pass
    
    @staticmethod
    def from_dict(data):
        user = User(
            age=data['age'],
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

    def __repr__(self):
        pass
