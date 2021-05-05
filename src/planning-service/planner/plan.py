from geopy import distance
from datetime import datetime

from planner.my_time import Time
from yelp_api import yelp


class Plan():

    def __init__(self, activities, coordinates, start_time, end_time):
        self.timer = Time(start_time, end_time)
        self.activities = activities
        self.plan = {}
        self.start_coordinates = coordinates
        self.activity_keys = []
        self.meal_keys = []
        self.walking_distance = (
            self.timer.duration/(200 + 2/self.timer.duration)
        )
        self.extract_nearby_meals_activities(activities)

    def extract_nearby_meals_activities(self, activities):
        for key, activity in activities.items():
            latitude = activity['coordinates'][0]
            longitude = activity['coordinates'][1]
            distance_to_activity = distance.distance(
                (latitude, longitude), self.start_coordinates).km
            if distance_to_activity <= self.walking_distance:
                meal = False
                for parent in activity['parents']:
                    if parent == 'Restaurants':
                        meal = True
                if meal:
                    self.meal_keys.append(key)
                else:
                    self.activity_keys.append(key)

    def create_plan(self):
        while self.timer.main_loop():
            if self.timer.is_meal_time():
                if self.add_meal():
                    self.timer.decriment_duration('meal')
            else:
                if self.add_activity():
                    self.timer.decriment_duration('activity')

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
            if exclude is False:
                self.plan[key] = activity
                self.activity_keys.remove(key)
                return True

    def add_meal(self):
        if not self.meal_keys:
            return False
        key = self.meal_keys.pop()
        self.plan[key] = self.activities[key]
        return True
