import requests
from geopy import distance
from datetime import datetime

import settings
from planner.my_time import Time
from yelp_api import yelp


class Plan():

    def __init__(self, activities, coordinates, start_time, end_time,
                 target_categories):
        self.timer = Time(start_time, end_time)
        self.activities = activities
        self.target_categories = target_categories
        self.start_coordinates = coordinates
        self.plan = {}
        self.position = 0
        self.activity_keys = []
        self.meal_keys = []
        self.yelp_searched = False
        self.visited = set()
        self.walking_distance = (
            self.timer.time_left/(200 + 2/self.timer.time_left)
        )
        self.extract_nearby_meals_activities(activities)

    def extract_nearby_meals_activities(self, activities):
        self.calculate_distances(activities)
        for key, activity in activities.items():
            if activity['distance'] <= self.walking_distance:
                meal = False
                for parent in activity['parents']:
                    if parent == 'Restaurants':
                        meal = True
                if meal:
                    self.meal_keys.append(key)
                else:
                    self.activity_keys.append(key)

    def calculate_distances(self, activities):
        for key, activity in activities.items():
            latitude = activity['coordinates'][0]
            longitude = activity['coordinates'][1]
            distance_to_activity = distance.distance(
                (latitude, longitude), self.start_coordinates).km
            activity['distance'] = distance_to_activity

    def create_plan(self):
        if not self.activity_keys or not self.meal_keys:
            self.search_yelp()
        while self.timer.main_loop():
            if self.timer.is_meal_time():
                if self.add_meal():
                    self.timer.decriment_time_left('meal')
                else:
                    return self.plan
            else:
                if self.add_activity():
                    self.timer.decriment_time_left('activity')
                else:
                    return self.plan

        return self.plan

    def add_activity(self):
        if not self.activity_keys:
            return False

        if self.timer.get_current_time() < datetime.strptime('18:00', '%H:%M'):
            excluded_categories = ['Bars', 'Nightlife']
        else:
            excluded_categories = ['Active Life']

        for key in self.activity_keys:
            activity = self.activities[key]
            exclude = False
            for parent in activity['parents']:
                if parent in excluded_categories:
                    exclude = True
            categories = set(self.activities[key]['categories'])
            visited_score = (
                len(self.visited.intersection(categories))/len(categories)
            )
            if visited_score >= 0.5:
                exclude = True
            if exclude is False:
                self.activity_keys.remove(key)
                self.add_to_plan(key)
                return True

        if self.yelp_searched:
            return False

        self.search_yelp()
        return self.add_activity()

    def add_meal(self):
        if not self.meal_keys:
            return False

        if self.timer.get_current_time() < datetime.strptime('18:00', '%H:%M'):
            excluded_categories = ['Bars', 'Nightlife']

        for key in self.meal_keys:
            activity = self.activities[key]
            exclude = False
            for parent in activity['parents']:
                if parent in excluded_categories:
                    exclude = True

            categories = set(self.activities[key]['categories'])
            visited_score = (
                len(self.visited.intersection(categories))/len(categories)
            )
            if visited_score >= 0.5:
                exclude = True
            if exclude is False:
                self.meal_keys.remove(key)
                self.add_to_plan(key)
                return True

        if self.yelp_searched:
            return False

        self.search_yelp()
        return self.add_meal()

    def add_to_plan(self, key):
        distance, time = self.get_graphhopper_distance(
            self.start_coordinates, self.activities[key]['coordinates']
        )
        self.timer.decriment_time_left('walk', time)
        self.activities[key]['position'] = self.position
        self.position += 1
        self.start_coordinates = self.activities[key]['coordinates']
        self.calculate_distances(self.activities)
        for category in self.activities[key]['categories']:
            self.visited.add(category)
        self.plan[key] = self.activities.pop(key)
        self.plan[key]['distance'] = distance
        self.plan[key]['time'] = time

    def search_yelp(self):
        activities = yelp.search_by_categories(
            self.target_categories,
            self.start_coordinates[0],
            self.start_coordinates[1],
            int(self.walking_distance*1000)
        )

        self.activities.update(activities)
        self.extract_nearby_meals_activities(activities)
        self.yelp_searched = True
        if self.activities:
            return True
        else:
            return False

    def get_graphhopper_distance(self, start, stop):
        params = {
            'point': [
                f'{start[0]},{start[1]}',
                f'{stop[0]},{stop[1]}'
            ],
            'vehicle': 'foot',
            'out_array': ['distances', 'times'],
            'key': settings.GRAPHH

        }
        response = requests.get(
            'https://graphhopper.com/api/1/matrix', params
        ).json()

        distance = response['distances'][0][1]/1000
        time = response['times'][0][1]/60
        return distance, time
