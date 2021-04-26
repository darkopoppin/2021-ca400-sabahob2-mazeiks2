import pandas as pd
import argparse
import json
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


parser = argparse.ArgumentParser(
                    description="Prototypes of recommendation algorithms")
parser.add_argument('-C', '--cosine', help="Cosine collaborative",
                    action='store_true')


def main():
    args = parser.parse_args()
    df = pd.read_csv("./filtered_dataset.csv")

    if args.cosine:
        cosine_sim_dataset(df)
    else:
        all_categories = []
        with open('my_categories.txt', "r") as f:
            line = f.readline()
            while line:
                all_categories.append(line.strip())
                line = f.readline()
            all_categories = ' '.join(all_categories)
        compare_profile_categories(all_categories)


def cosine_sim_dataset(df):
    cv = CountVectorizer()
    print(df)
    count_matrix = cv.fit_transform(df['Categories'])
    print(cv.vocabulary_)
    print(df.loc[[6280]])
    cosine_values = cosine_similarity(count_matrix[6280], count_matrix)
    similar_items = list(enumerate(cosine_values[0]))
    print(cosine_values)
    print("Similar items:")
    sorted_similar = sorted(similar_items, key=lambda x: x[1], reverse=True)
    for item in sorted_similar:
        if item[1] > 0.8:
            print(f'{item} - {df.loc[item[0], "Categories"]}')
    

def compare_profile_categories(all_categories):
    user_one = None
    user_two = None

    with open('./users/user_profile_one.json', 'r') as f:
        user_one = json.load(f)
    
    with open('./users/user_profile.json', 'r') as f:
        user_two = json.load(f)
        
    user_one_categories = set(user_one['liked_categories'])
    user_two_categories = set(user_two['liked_categories'])

    intersection = user_two_categories.intersection(user_one_categories)
    
    if len(intersection)/len(user_one_categories) > 0.7:
        print(len(intersection)/len(user_one_categories))
    else:
        print(len(intersection)/len(user_one_categories))

    cosine_collab(all_categories)

    possible_interest = list(user_two_categories.difference(user_one_categories))
    #cosine_new_recommendations(possible_interest)

def cosine_collab(all_categories):
    with open('./users/user_one.json', 'r') as f:
        user_one = json.load(f)
    
    with open('./users/user.json', 'r') as f:
        user_two = json.load(f)
    
    user_one_categories = [all_categories]
    user_two_categories = [all_categories]
    for poi_one, poi_two in zip(user_one, user_two):
        if poi_one['rating'] == 1:
            user_one_categories.append(' '.join(poi_one['categories']))
        if poi_two['rating'] == 1:
            user_two_categories.append(' '.join(poi_two['categories']))        
    
    cv = CountVectorizer()
    count_matrix_one = cv.fit_transform(user_one_categories)
    count_matrix_two = cv.fit_transform(user_two_categories)
    cosine_values = cosine_similarity(count_matrix_one[1:], count_matrix_two[1:])
    print(cosine_values)
    
if __name__ == '__main__':
    main()
