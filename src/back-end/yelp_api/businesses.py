import time
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

transport = RequestsHTTPTransport(
    url='https://api.yelp.com/v3/graphql',
    headers={
        'Authorization': 'Bearer f-625oQS3C7MH4ksSS2Bz30c5vtkbg669c4DHqzqrrmMStzihXNwEClzXZ6vrya_38Ol2aw0Inf6z90IePHjjAG7UZGCDhXbP3hhskIGaiyygD15bhvUtqsb6swjYHYx',
        'Content-Type': 'application/json'
    })
client = Client(
    transport=transport,
    fetch_schema_from_transport=True,
)


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
    results = client.execute(query, variable_values=params)

    finish = time.perf_counter()
    print(f'{finish - start}')
    return results
