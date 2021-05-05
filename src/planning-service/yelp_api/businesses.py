import json
from os import path
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

import settings


class Yelp(object):

    def __init__(self):
        transport = RequestsHTTPTransport(
            url='https://api.yelp.com/v3/graphql',
            headers={
                'Authorization': 'Bearer ' + settings.YELP_API,
                'Content-Type': 'application/json'
            })

        self.yelp_client = Client(
            transport=transport,
            fetch_schema_from_transport=True,
        )

        with open(str(path.dirname(__file__)) + '/alias_mappings.json') as f:
            self.alias_mappings = json.load(f)

    def search_by_categories(self, categories, latitude, longitude, radius):
        aliases = self.map_titles_to_aliases(categories)
        query_string = ['query search($lat: Float! $long: Float! $rad: Float!']
        params = {
            'lat': latitude,
            'long': longitude,
            'rad': radius
        }
        for i in range(len(aliases)):
            params.update({f'category{i}': aliases[i]})
            query_string.append(f'$category{i}: String! ')
        query_string.append(') {')

        for i in range(len(aliases)):
            query_string.append(f's{i}: search(categories: $category{i},')
            query_string.append('limit: 50, latitude: $lat, longitude: $long,')
            query_string.append('radius: $rad) ')
            query_string.append('{business {id url rating categories')
            query_string.append('{title parent_categories {title}}')
            query_string.append('coordinates { latitude longitude }}}')
        query_string.append('} ')

        query = gql(''.join(query_string))
        results = self.yelp_client.execute(query, variable_values=params)

        businesses = self.format_search_results(results)
        return businesses

    def map_titles_to_aliases(self, categories):
        aliases = []
        for i in range(len(categories)):
            aliases.append(self.alias_mappings[categories[i]])
        return aliases

    def format_search_results(self, results):
        businesses = {}
        s = 0
        for search, result in results.items():
            b = 0
            for business in result['business']:
                fields = {}
                categories = []
                parents = set()
                for category in business['categories']:
                    categories.append(category['title'])
                    for parent in category['parent_categories']:
                        parents.add(parent['title'])

                fields['categories'] = categories
                fields['parents'] = list(parents)
                fields['id'] = business['id']
                fields['rating'] = business['rating']
                fields['coordinates'] = (
                    business['coordinates']['latitude'],
                    business['coordinates']['longitude']
                )
                fields['url'] = business['url']
                fields['rating'] = business['rating']
                businesses.update({f's{str(s)}{str(b)}': fields})
                b += 1
            s += 1

        return businesses
