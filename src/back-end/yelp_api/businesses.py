from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from multiprocessing.pool import ThreadPool

import time


class YelpGQL(object):
    client = None

    def __init__(self):
        sample_transport = RequestsHTTPTransport(
            url='https://api.yelp.com/v3/graphql',
            headers={
                'Authorization': 'Bearer f-625oQS3C7MH4ksSS2Bz30c5vtkbg669c4DHqzqrrmMStzihXNwEClzXZ6vrya_38Ol2aw0Inf6z90IePHjjAG7UZGCDhXbP3hhskIGaiyygD15bhvUtqsb6swjYHYx',
                'Content-Type': 'application/json'
            })
        self.client = Client(
            transport=sample_transport,
            fetch_schema_from_transport=True,
        )

    def get_business_info(self, business_id):
        params = {"code": business_id}
        query = gql('''
        query business($code: String!)
        {
            business(id: $code) {
                name
                id
                rating
                price
                location {
                    address1
                }
            }
        }
        ''')
        try:
            result = self.client.execute(query, variable_values=params)
        except Exception:
            # business doesn't exist on YELP
            return None

        return result['business']

    def get_n_businesses_info(self, ids):
        pool = ThreadPool(6)

        start = time.perf_counter()

        results = pool.map_async(self.get_business_info, ids)
        pool.close()
        pool.join()

        finish = time.perf_counter()
        print(f'{finish - start}')
        return results

    def search_by_categories(self, category):
        params = {'category': category}
        query = gql('''
        query search($category: String!)
        {
            search(categories: $category,
                   limit: 50,
                   location: "dublin") {
                total
                business {
                    id
                    categories
                }
            }
        }
        ''')
        try:
            result = self.client.execute(query, variable_values=params)
        except Exception:
            # business doesn't exist on YELP
            return None
        
        print(result)
