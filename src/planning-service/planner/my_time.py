class Time(object):
    def __init__(self, start_time, end_time):
        self.start_time = (int(start_time[0]), int(start_time[1]))
        self.end_time = (int(end_time[0]), int(end_time[1]))
        self.duration = (((self.end_time[0] - self.start_time[0]) * 60)
                         + self.end_time[1] + self.start_time[1])
        self.meal_timer = 180

    def decriment_duration(self, activity):
        if activity == 'meal':
            self.duration -= 60
            self.meal_timer = 180
        elif activity == 'activity':
            self.duration -= 45
            self.meal_timer -= 45

    def main_loop(self):
        if self.duration <= 30:
            return False
        else:
            return True

    def is_meal_time(self):
        if self.meal_timer <= 20:
            return True
        else:
            return False

    def __repr__(self):
        return (
            f'Duration: {self.duration} mins\n'
            f'Start time: {self.start_time}\n'
            f'End time: {self.end_time}\n')
