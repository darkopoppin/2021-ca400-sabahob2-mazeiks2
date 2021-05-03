from models.user import User


class TestUser():

    def create_user(self, test_user):
        return User(
            test_user['user_id'],
            test_user['age'],
            test_user['gender'],
            test_user['location'],
            test_user['liked_categories']
        )

    def test_creating_user(self, test_user):
        user = self.create_user(test_user)

        assert test_user['user_id'] == user.user_id
        assert test_user['age'] == user.age
        assert test_user['gender'] == user.gender
        assert test_user['location'] == user.location
        assert test_user['liked_categories'] == user.liked_categories
        assert {} == user.visited

    def test_to_dict(self, test_user):
        user = self.create_user(test_user)
        user_dict = user.to_dict()
        # to_dict() does not include the user_id
        user_dict['user_id'] = user.user_id
        assert test_user == user_dict

    def test_saving_user(self, test_db, test_user):
        user = self.create_user(test_user)
        user.save()
        user_ref = test_db.collection('users').document(test_user['user_id']).get()

        assert user_ref.exists is True

    def test_update_categories(self, test_db, test_user):
        test_user['liked_categories'].append('Bars')

        user = self.create_user(test_user)

        user.update_categories()
        user_ref = test_db.collection('users').document(test_user['user_id']).get()
        user_categories = user_ref.to_dict().get('liked_categories')
        assert user.liked_categories == user_categories

    def test_from_dict(self, test_db, test_user):
        user_ref = test_db.collection('users').document(test_user['user_id']).get()
        user = user_ref.to_dict()

        assert test_user['age'] == user['age']
        assert test_user['gender'] == user['gender']
        assert test_user['location'] == user['location']
        assert test_user['liked_categories'] == user['liked_categories']
        assert {} == user['visited']
