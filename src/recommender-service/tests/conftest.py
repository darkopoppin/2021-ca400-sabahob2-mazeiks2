import pytest
import json
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from os import environ
from firebase_admin import firestore

from service import create_service


@pytest.fixture(scope='session')
def test_client():
    app = create_service()
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture(scope='session')
def test_db():
    db = firestore.client()
    yield db


@pytest.fixture(scope='module')
def yelp_client():
    sample_transport = RequestsHTTPTransport(
        url='https://api.yelp.com/v3/graphql',
        headers={
            'Authorization': 'Bearer ' + environ.get('YELP_API'),
            'Content-Type': 'application/json'
        })
    client = Client(
        transport=sample_transport,
        fetch_schema_from_transport=True,
    )
    yield client
    client.close()


@pytest.fixture(scope='function')
def alias_mappings():
    with open('./yelp_api/alias_mappings.json') as f:
        yield json.load(f)


@pytest.fixture(scope='function')
def yelp_categories(yelp_client):
    query = gql(
        '''
        {categories {
            category {
            title
            alias
            }
        } }
        '''
    )
    results = yelp_client.execute(query)
    return results['categories']['category']
