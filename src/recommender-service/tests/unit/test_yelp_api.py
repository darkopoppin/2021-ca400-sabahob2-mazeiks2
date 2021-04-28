from yelp_api import format_search_results
from gql import gql


def test_map_titles_to_aliases(alias_mappings, yelp_categories):
    successful_mappings = 0
    for category in yelp_categories:
        try:
            alias_mappings[category['title']]
            successful_mappings += 1
        except KeyError:
            pass
    assert successful_mappings == len(alias_mappings.keys())


def test_format_search_results(yelp_client):
    query = gql(
        '''
        {b1: search(
            categories: "german",
            limit: 50,
            location: "dublin")
            {business {id categories {title}}}}
        '''
    )
    result = yelp_client.execute(query)
    business = format_search_results(result)

    b1 = result['b1']['business'][0]
    assert b1['id'] in business.keys()
    assert len(b1['categories']) == len(business[b1['id']])
