from planner.my_time import Time
from planner.plan import Plan


def create_plan(activities, start_time, end_time, coordinates):
    time = Time(start_time, end_time)
    planner = Plan(activities, coordinates)
    while time.main_loop():
        if time.is_meal_time():
            print('Meal time')
            time.decriment_duration('meal')
        else:
            print('Activity time')
            time.decriment_duration('activity')
        print(time)
