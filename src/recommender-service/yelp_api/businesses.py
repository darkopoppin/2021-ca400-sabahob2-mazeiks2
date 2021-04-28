import time
import json
from os import path
from gql import gql

from yelp_api import yelp_client

with open(str(path.dirname(__file__)) + '/alias_mappings.txt') as f:
    alias_mappings = json.load(f)


def search_by_categories(categories):
    map_titles_to_aliases(categories)

    start = time.perf_counter()
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
    results = yelp_client.execute(query, variable_values=params)

    finish = time.perf_counter()
    print(f'{finish - start}')

    businesses = format_search_results(results)
    return businesses


def map_titles_to_aliases(categories):
    global alias_mappings
    for i in range(len(categories)):
        categories[i] = alias_mappings[categories[i]]


def format_search_results(results):
    businesses = {}
    for search, result in results.items():
        for business in result['business']:
            categories = [
                category['title'] for category in business['categories']
                ]
            businesses.update({business['id']: categories})

    return businesses
