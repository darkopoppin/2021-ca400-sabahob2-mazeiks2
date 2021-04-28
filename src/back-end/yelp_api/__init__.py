from gql import Client
from gql.transport.requests import RequestsHTTPTransport

import settings


transport = RequestsHTTPTransport(
    url='https://api.yelp.com/v3/graphql',
    headers={
        'Authorization': 'Bearer ' + settings.YELP_API,
        'Content-Type': 'application/json'
    })

yelp_client = Client(
    transport=transport,
    fetch_schema_from_transport=True,
)

from .businesses import *
