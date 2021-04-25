from yelp_api import get_businesses_info, search_yelp


def test_get_business_info():
    ids = [
        'TYzPPCO4ZWHQaeub7JSDXw',
        '9Qh4znoHA5oK7utia60A7A',
        'yfd57peLvJlAlP4Apr_Zlw'
        ]

    result = get_businesses_info(ids)
    assert len(ids) == len(result.keys())
    for business, fields in result.items():
        assert len(fields) == 4
        assert 'id' in fields
        assert 'location' in fields
        assert 'address1' in fields['location']
        assert 'name' in fields
        assert 'rating' in fields


def test_search_yelp():
    term = "French restaurant"
    location = 'Dublin'

    results = search_yelp(term, location)['business']

    assert len(results) == 20
    for business in results:
        fields = business.keys()
        assert len(fields) == 6
        assert 'location' in fields
        assert 'name' in fields
        assert 'rating' in fields
        assert 'price' in fields
        assert 'categories' in fields
        assert 'review_count' in fields
