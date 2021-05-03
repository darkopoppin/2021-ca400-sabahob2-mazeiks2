import argparse
import json
import firebase_admin
import random
from os import environ, path
from firebase_admin import credentials
from firebase_admin import firestore
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Firebase
cred = credentials.Certificate('./src/recommender-service/credentials/citycydev-firebase.json')
firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://citycydev-default-rtdb.firebaseio.com'
})
db = firestore.client()

# YELP
transport = RequestsHTTPTransport(
    url='https://api.yelp.com/v3/graphql',
    headers={
        'Authorization': 'Bearer ' + environ.get('YELP_API'),
        'Content-Type': 'application/json'
    })
client = Client(
    transport=transport,
    fetch_schema_from_transport=True,
)

parser = argparse.ArgumentParser(
    description="Uploads a dataset of businesses ")

with open(str(path.dirname(__file__)) + '/my_categories.txt') as f:
    alias_mappings = json.load(f)


def recommend_new_users():
    users = db.collection('users').stream()
    for user in users:
        user_dict = user.to_dict()
        if len(user_dict['visited']) == 0:
            businesses = search_by_categories(user_dict['liked_categories'])
            visited = {}
            n = random.randrange(1,20)
            keys = list(businesses.keys())
            random.shuffle(keys)
            for key in keys:
                categories = businesses[key]
                visited.update({
                    key: {
                        'rating': random.randrange(1, 6),
                        'categories': categories
                    }
                })
                n -= 1
                if n == 0:
                    break
            print(user.id)
            db.collection('users').document(user.id).update({'visited': visited})


def search_by_categories(categories):
    map_titles_to_aliases(categories)

    query_string = ['query search(']
    params = {}
    for i in range(len(categories)):
        params.update({f'category{i}': categories[i]})
        query_string.append(f'$category{i}: String! ')
    query_string.append(') {')

    for i in range(len(categories)):
        query_string.append(f's{i}: search(categories: $category{i},')
        query_string.append('limit: 50, location: "dublin")')
        query_string.append('{business {id categories {title}}}')
    query_string.append('} ')

    query = gql(''.join(query_string))
    results = client.execute(query, variable_values=params)

    businesses = format_search_results(results)
    return businesses


def format_search_results(results):
    businesses = {}
    for search, result in results.items():
        for business in result['business']:
            categories = [
                category['title'] for category in business['categories']
                ]
            businesses.update({business['id']: categories})

    return businesses


def map_titles_to_aliases(categories):
    global alias_mappings
    for i in range(len(categories)):
        categories[i] = alias_mappings[categories[i]]


def main():
    recommend_new_users()


if __name__ == '__main__':
    main()
