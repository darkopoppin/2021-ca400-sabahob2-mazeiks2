from planner.plan import Plan


def create_plan(activities, start_time, end_time, coordinates):
    planner = Plan(activities, coordinates, start_time, end_time)
    while planner.main_loop():
        print(planner)
        if planner.is_meal_time():
            if planner.add_meal():
                planner.decriment_duration('meal')
        else:
            if planner.add_activity():
                planner.decriment_duration('activity')

    return planner.plan
