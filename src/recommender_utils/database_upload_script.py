import argparse
import json
import firebase_admin
import random
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('../recommender_service/credentials/citycydev-firebase.json')
firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://citycydev-default-rtdb.firebaseio.com'
})
db = firestore.client()

parser = argparse.ArgumentParser(description="Uploads a dataset of businesses ")

def main():
    with open('filtered_dataset.json', 'r') as f:
        dataset = json.load(f)

    users = {'users':{}}
    categories = set()
    visited = {}
    for i in range(0, 10):
        for j in range(0, 20):
            poi_id = random.randrange(0, len(dataset))
            poi = dataset[poi_id]
            poi['rating'] = random.randrange(1,6)
            if 4 <= poi['rating'] <= 5:
                categories.update(set(poi['categories']))
            visited.update({
                poi['business_id']:{
                    'rating': poi['rating'],
                    'categories': poi['categories']
                }
            })
        
        user_profile = {
            'id': i,            
            'age': random.randrange(20, 30),
            'gender': random.sample(['male', 'female'],1)[0],
            'liked_categories': list(categories),
            'visited': visited
        }

        users['users'].update({i: user_profile})
    
        doc_ref = db.collection(u'users')
        doc_ref.add(user_profile)

if __name__ == '__main__':
    main()
