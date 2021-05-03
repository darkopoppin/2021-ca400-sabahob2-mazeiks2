from geopy import distance


class Plan(object):
    def __init__(self, activities, coordinates):
        self.activities = activities
        self.plan = []
        self.travel_time = []
        self.coordinates = coordinates
        self.filtered_keys = []

        for key, activity in activities.items():
            longitude = activity['coordinates']['longitude']
            latitude = activity['coordinates']['latitude']
            distance_to_activity = distance.distance(
                (latitude, longitude), coordinates).km
            if distance_to_activity <= 5:
                self.filtered_keys.append(key)

    def add_activity(self):
        pass

    def add_meal(self):
        pass
