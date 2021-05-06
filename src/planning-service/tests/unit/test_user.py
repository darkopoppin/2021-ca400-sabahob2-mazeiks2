from planner.user import User

class TestUser():

    def create_user(self, test_user):
        return User(
            'FBUmHzsMQcEl6KAiAzNB',
            test_user['age'],
            test_user['gender'],
            test_user['location'],
            test_user['liked_categories'],
            test_user['visited']
        )

    def test_creating_user(self, test_user):
        user = self.create_user(test_user)

        assert 'FBUmHzsMQcEl6KAiAzNB' == user.user_id
        assert test_user['age'] == user.age
        assert test_user['gender'] == user.gender
        assert test_user['location'] == user.location
        assert test_user['liked_categories'] == user.liked_categories
        assert test_user['visited'] == user.visited

    def test_to_dict(self, test_user):
        user = self.create_user(test_user)
        user_dict = user.to_dict()
        print(user_dict)
        # to_dict() does not include the user_id
        user_dict['user_id'] = user.user_id
        user_dict.pop('user_id')
        assert test_user == user_dict

    def test_from_dict(self, test_db, test_user):
        user_ref = test_db.collection('users').document('FBUmHzsMQcEl6KAiAzNB').get()
        user = user_ref.to_dict()

        assert test_user['age'] == user['age']
        assert test_user['gender'] == user['gender']
        assert test_user['location'] == user['location']
        assert test_user['liked_categories'] == user['liked_categories']
        assert test_user['visited'] == user['visited']
