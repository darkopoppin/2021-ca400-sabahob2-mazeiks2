import json
import random
import argparse
import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser(description="Extracts all the values of a key in a business.\
                    Filter the categories.")
parser.add_argument("-e", "--extract",
                    help="Extracts the values of the passed key")
parser.add_argument("-f", "--filter", help="Filter the categories",
                    action='store_true')
parser.add_argument("-c", "--categories",
                    help="Extract the required categories from the YELP json")
parser.add_argument('-s', '--statistics',
                    help="Statistics")
parser.add_argument('-r', '--reviews',
                    help="Extract reviews of the businesses from \
                    filtered_dataset.json")
parser.add_argument('-C', '--csv', help="Save the json dataset as csv")
parser.add_argument('-U', '--user', help="Create a dummy user",
                    action='store_true')

# not interested in theses parent categories
not_relevant_parents = set([
    'Automotive',
    'Beauty & Spas',
    'Bicycles',
    'Education',
    'Event Planning & Services',
    'Financial Services',
    'Health & Medical',
    'Home Services',
    'Hotels & Travel',
    'Local Services',
    'Mass Media',
    'Pets',
    'Professional Services',
    'Public Services & Government',
    'Real Estate',
    'Religious Organizations',
    'Shopping',
])

relevant_parents = ['Active Life', 'Nightlife', 'Local Flavor', 'Arts & Entertainment', 'Restaurants']
restaurants = {}


def main():
    businesses = open_json("yelp_academic_dataset_business.json")
    args = parser.parse_args()

    if args.extract:
        extract(businesses, args.extract)

    if args.categories:
        with open(args.categories, "r") as f:
            categories = json.load(f)

        extract_categories(categories)

    if args.filter:
        categories = []
        with open('my_categories.txt', "r") as f:
            line = f.readline()
            while line:
                categories.append(line.strip())
                line = f.readline()

        filter_categories(businesses, categories)

    if args.statistics:
        generate_statistics(args.statistics)

    if args.reviews:
        get_reviews(args.reviews)

    if args.csv:
        convert_to_csv(args.csv)

    if args.user:
        create_user()


def open_json(path):
    data = []
    with open(path, "r") as f:
        for line in f:
            data.append(json.loads(line))
    data.sort(key=lambda item: item["name"].strip())
    return data


def extract(data, target):
    cities = {}
    for business in data:
        city = business[target]
        if city in cities:
            cities[city] += 1
        else:
            cities[city] = 1

    sorted_values = sorted(cities.items(), key=lambda item: item[1])
    print(len(cities))
    print(sorted_values)


def extract_categories(categories):
    my_categories = []
    parent_categories = [
        "active",
        "arts",
        "localflavor",
        "tours",
        "nightlife",
        "restaurants",
    ]
    # some parent categories have sub categories that have to be avoided
    avoid_categories = [
        'fitness',
        'gourmet'
    ]
    cuisine_endings = ['an', 'se', 'ne', 'hi', 'sh', 'ch', 'no', 'nd']
    with open('my_categories.txt', 'w') as f:
        for category in categories:
            for parent in category['parents']:
                if (parent in parent_categories and
                        parent not in avoid_categories):
                    if parent == 'restaurants':
                        if category['alias'][-2:] in cuisine_endings:
                            print(category['title'])
                            title = category['title']
                            f.write(f'{title}\n')
                    else:
                        title = category['title']
                        f.write(f'{title}\n')

    return my_categories


def filter_categories(businesses, my_categories):
    filtered = []
    my_categories = set(my_categories)
    global not_relevant_parents

    print("Filtering categories...")
    for business in businesses:
        if (business['categories'] is not None):
            full_categories = set(business['categories'].split(', '))
            categories = full_categories.difference(not_relevant_parents)
            filtered_categories = categories.intersection(my_categories)

            # 1009 businesses have only parent categories
            if ((len(filtered_categories) == 1 and
                    list(filtered_categories)[0] in relevant_parents) or
                    len(categories) == 0):
                interest_percent = 0
            else:
                interest_percent = len(filtered_categories)/len(categories)

            if (interest_percent >= 0.7 and restaurant_reducer(filtered_categories) and not repeated(business, filtered)):
                filtered.append({
                    "business_id": business["business_id"],
                    "name": business["name"],
                    "stars": business["stars"],
                    "review_count": business["review_count"],
                    "categories": list(filtered_categories)
                })
                print(len(filtered), flush=True)

    print(f'Filtered: {len(filtered)}')
    print(f'All: {len(businesses)}')

    print("Saving json...")
    with open("filtered_dataset.json", "w") as f:
        json.dump(filtered, f, indent=4)


def repeated(business, businesses):
    name = business['name']
    for b in businesses:
        if name == b['name']:
            return True
    return False


def restaurant_reducer(categories):
    global restaurants

    if 'Restaurants' not in categories:
        return True

    for category in categories:
        if category in restaurants and restaurants.get(category, 100) < 30:
            restaurants[category] += 1
            return True
        elif category not in restaurants:
            restaurants[category] = 1
            return True
    return False


def generate_statistics(path):
    number_activities_per_category = {}
    reviews_per_business = []
    parent_categories = set([
        'Active Life',
        'Arts & Entertainment',
        'Restaurants',
        'Nightlife',
        'Local Flavor'])

    with open(path, 'r') as f:
        dataset = json.load(f)

    for business in dataset:
        categories = set(business['categories']).intersection(
            parent_categories
        )
        reviews_per_business.append(business['review_count'])
        for category in categories:
            if category in number_activities_per_category:
                number_activities_per_category[category] += 1
            else:
                number_activities_per_category[category] = 0

    median_deviation(reviews_per_business)
    print(number_activities_per_category)
    histogram_reviews(reviews_per_business)


def histogram_reviews(reviews_count):
    fig, ax = plt.subplots(1, 1)
    # logbins = np.logspace(np.log10(reviews_count[0]))
    ax.hist(reviews_count, bins=list(range(0, 1000, 100)))
    ax.set_title("Number of reviews per business")
    ax.set_xticks(list(range(0, 1000, 100)))
    plt.yscale('log')
    ax.set_xlabel("Number of reviews")
    ax.set_ylabel("Number of businesses (log scaled)")
    plt.show()


def median_deviation(reviews_count):
    x = stats.median_abs_deviation(reviews_count)
    mean = np.median(reviews_count)
    print(f"Median of the reviews per business: {mean}")
    print(f"Median absolute deviation: {x}")


def get_reviews(path):
    with open(path, 'r') as f:
        dataset = json.load(f)

    reviews = open_json('yelp_academic_dataset_review.json')
    stop = 0
    for business in dataset:
        if stop == 4:
            break
        for review in reviews:
            if business['business_id'] == review['business_id']:
                print(review['text'])
        stop += 1


def convert_to_csv(path):
    with open(path, 'r') as f:
        dataset = json.load(f)

    data = {}
    columns = ['Id', 'Name', 'Categories']

    data['Id'] = []
    data['Name'] = []
    data['Categories'] = []
    for business in dataset:
        data['Id'].append(business['business_id'])
        data['Name'].append(business['name'])
        data['Categories'].append(' '.join(business['categories']))

    df = pd.DataFrame(data, columns=columns)
    df.to_csv('path')


def create_user():
    with open('filtered_dataset.json', 'r') as f:
        dataset = json.load(f)

    user = []
    for i in range(0, 10):
        poi_id = random.randrange(0, len(dataset))
        poi = dataset[poi_id]
        user.append(poi)

    print(user)


if __name__ == "__main__":
    main()
