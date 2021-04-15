import time
import json

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from multiprocessing.pool import ThreadPool


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
        with open('./src/recommender-service/alias_mappings.txt') as f:
            self.alias_mappings = json.load(f)

    def search_by_category(self, category):
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
                    categories {
                        title
                        alias
                    }
                }
            }
        }
        ''')
        result = self.client.execute(query, variable_values=params)

        return result['search']

    def search_by_categories(self, categories):

        for i in range(len(categories)):
            categories[i] = self.alias_mappings[categories[i]]

        pool = ThreadPool(2)

        start = time.perf_counter()

        results = pool.map_async(self.search_by_category, categories)
        pool.close()
        pool.join()

        finish = time.perf_counter()
        print(f'{finish - start}')
        return results
