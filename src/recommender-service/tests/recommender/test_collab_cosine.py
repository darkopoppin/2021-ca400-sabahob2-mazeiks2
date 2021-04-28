from gql import gql
from recommenders.collab_cosine import collab_cosine
from recommenders.utils import get_similar_users


def test_collab_cosine(test_db, yelp_client):
    users = test_db.collection('users').stream()
    accuracy = []
    diversity = []
    quality = []
    for user in users:
        related_users = get_similar_users(user)
        recommendations = collab_cosine(user, related_users)

        if len(recommendations) != 0:
            print(user.id)
            user_visited = user.to_dict().get('visited')
            user_categories = set()
            for business, fields in user_visited.items():
                categories = ' '.join(fields['categories']).split()
                for category in categories:
                    user_categories.add(category)

            recommended_categories = set()
            for key, fields in recommendations.items():
                categories = fields['categories'].split()
                for category in categories:
                    recommended_categories.add(category)

            intersected = recommended_categories.intersection(user_categories)
            accuracy.append(len(intersected) / len(user_categories))
            diversity.append(
                len(recommended_categories - intersected) / len(recommended_categories)
            )
            quality.append(calculate_quality(yelp_client, recommendations))

    print(f'Accuracy: {sum(accuracy)/len(accuracy)}')
    print(f'Diversity: {sum(diversity)/len(diversity)}')
    print(f'Quality: {sum(quality)/len(quality)}')


def calculate_quality(yelp_client, recommendations):
    ratings = get_yelp_ratings(yelp_client, list(recommendations.keys()))
    mean_yelp_rating = sum(ratings) / len(ratings)
    return mean_yelp_rating


def get_yelp_ratings(client, ids):
    query_string = ['query business(']
    params = {}
    for i in range(len(ids)):
        params.update({f'id{i}': ids[i]})
        query_string.append(f'$id{i}: String! ')
    query_string.append(') {')

    for i in range(len(ids)):
        query_string.append(f'b{i}: business(id: $id{i})')
        query_string.append('{...Info}')
    query_string.append('} ')
    query_string.append('fragment Info on Business \
                        {id rating}')

    query = gql(''.join(query_string))
    results = client.execute(query, variable_values=params)

    ratings = []
    for business, fields in results.items():
        ratings.append(fields['rating'])
    
    return ratings
