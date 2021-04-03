from service import db


def get_similar_users(user_profile):
    user = user_profile.to_dict()
    age = user.get('age')
    gender = user.get('gender')
    users_query = (
        db.collection('users')
        .where('gender', '==', gender)
        .order_by('age')
        .start_at({'age': age - 2})
        .end_at({'age': age + 2})
        .stream()
    )

    return users_query
