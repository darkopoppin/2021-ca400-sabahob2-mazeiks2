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

    def compile_business_query(self, ids, type):
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

        if type == 'planner':
            query_string.append('fragment Info on Business \
                                {id rating url location {address1} \
                                categories {title parent_categories {title}} \
                                coordinates {latitude,longitude}}')
        else:
            query_string.append('fragment Info on Business \
                                {id name rating location {address1} \
                                url categories {title}}')

        query = gql(''.join(query_string))
        results = self.yelp_client.execute(query, variable_values=params)

        return results

    def search_yelp(self, term, location):
        query = gql('''
            query search($term: String! $loc: String!)
            {
                search(term: $term, location: $loc) {
                    business {
                        name
                        rating
                        price
                        review_count
                        location {
                            address1
                            city
                        }
                        categories {
                            title
                        }
                    }
                }
            }
        ''')
        params = {
            'term': term,
            'loc': location
        }
        results = self.yelp_client.execute(query, variable_values=params)

        return results['search']

    def get_businesses_info(self, ids):
        results = self.compile_business_query(ids, 'recommender')
        return results

    def get_businesses_info_planner(self, ids):
        results = self.compile_business_query(ids, 'planner')
        formatted = self.format_for_planner(results)
        return formatted

    def format_for_planner(self, ids):
        formatted = {}
        for key, business in ids.items():
            fields = {}
            categories = []
            parents = set()
            for category in business['categories']:
                categories.append(category['title'])
                for parent in category['parent_categories']:
                    parents.add(parent['title'])
            fields['id'] = business['id']
            fields['categories'] = categories
            fields['parents'] = list(parents)
            fields['coordinates'] = (
                business['coordinates']['latitude'],
                business['coordinates']['longitude']
            )
            fields['url'] = business['url']
            fields['rating'] = business['rating']
            formatted[key] = fields

        return formatted
