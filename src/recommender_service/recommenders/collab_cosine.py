from gql import Client, gql
import json
from gql.transport.requests import RequestsHTTPTransport
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


def collab_cosine(user_profile, related_users):
    user = user_profile.to_dict()

    potential_reccomms = {}
    for related_user in related_users:
        if user_profile.id != related_user.id:
            user_score = calculate_user_score(user, related_user)
            related_user_dict = related_user.to_dict()

            for poi_id in related_user_dict['visited'].keys():
                rating = related_user_dict['visited'][poi_id]['rating']
                categories = related_user_dict['visited'][poi_id]['categories']

                if potential_reccomms.get(poi_id):
                    potential_reccomms[poi_id]["poi_score"] += 1
                    if user_score > potential_reccomms[poi_id]["user_score"]:
                        potential_reccomms[poi_id]["user_score"] = user_score
                elif 4 <= rating <= 5:
                    potential_reccomms[poi_id] = {
                        "user_score": user_score,
                        "poi_score": 1,
                        "categories": ' '.join(categories)
                    }

    user_history = []
    for poi_id in user['visited'].keys():
        categories = user['visited'][poi_id]['categories']
        rating = user['visited'][poi_id]['rating']
        if 4 <= rating <= 5:
            user_history.append(' '.join(categories))

    cv = CountVectorizer()
    for poi_id in potential_reccomms.keys():
        pois_categories = user_history
        pois_categories.append(potential_reccomms[poi_id]['categories'])
        count_matrix = cv.fit_transform(pois_categories)
        cosine_values = cosine_similarity(count_matrix[-1], count_matrix[:-1])

        user_score = potential_reccomms[poi_id]['user_score']
        poi_score = potential_reccomms[poi_id]['poi_score'] / len(pois_categories)
        score = cosine_values.max() * 100 * user_score * poi_score
        potential_reccomms[poi_id]['final_score'] = score

    # print(json.dumps(potential_reccomms, indent=4))
    sorted_recommendations = sorted(
        potential_reccomms.items(),
        key=lambda x: x[1]['final_score'],
        reverse=True)
    print(json.dumps(sorted_recommendations, indent=4))


def calculate_user_score(user, related_user):
    user_categories = set(user['liked_categories'])
    related_user = related_user.to_dict()
    related_user_categories = set(related_user['liked_categories'])

    intersection = related_user_categories.intersection(user_categories)
    union = related_user_categories.union(user_categories)

    user_score = len(intersection) / len(union)
    return user_score


def request_categories(business_id):
    print(business_id)
    sample_transport = RequestsHTTPTransport(
        url='https://api.yelp.com/v3/graphql',
        headers={
            'Authorization': 'Bearer f-625oQS3C7MH4ksSS2Bz30c5vtkbg669c4DHqzqrrmMStzihXNwEClzXZ6vrya_38Ol2aw0Inf6z90IePHjjAG7UZGCDhXbP3hhskIGaiyygD15bhvUtqsb6swjYHYx',
            'Content-Type': 'application/json'
        })
    client = Client(
        transport=sample_transport,
        fetch_schema_from_transport=True,
    )
    params = {"code": business_id}
    query = gql('''
    query business($code: String!)
    {
        business(id: $code) {
            name
            id
            categories{
                title
            }
        }
    }
    ''')
    result = client.execute(query, variable_values=params)
    print(result)
    return result.get('categories')