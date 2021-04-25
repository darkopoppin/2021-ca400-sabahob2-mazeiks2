import time
from gql import gql

from yelp_api import yelp_client


def get_businesses_info(ids):
    start = time.perf_counter()

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
                        {id name rating location {address1}}')

    query = gql(''.join(query_string))
    results = yelp_client.execute(query, variable_values=params)

    finish = time.perf_counter()
    print(f'{finish - start}')
    return results


def search_yelp(term, location):
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
    results = yelp_client.execute(query, variable_values=params)

    return results['search']
