from datetime import datetime, timedelta


class Time(object):

    def __init__(self, start_time, end_time):
        self.start_time = start_time[0] + ':' + start_time[1]
        self.end_time = end_time[0] + ':' + end_time[1]
        date_format = '%H:%M'
        self.time_left = (
            (datetime.strptime(self.end_time, date_format) -
                datetime.strptime(self.start_time, date_format)).seconds / 60
        )
        self.meal_timer = 180

    def decriment_time_left(self, activity, time=None):
        if activity == 'meal':
            self.time_left -= 60
        elif activity == 'activity':
            self.time_left -= 45
            self.meal_timer -= 45
        else:
            self.time_left -= time

    def get_current_time(self):
        date_format = '%H:%M'
        current_time = (
            datetime.strptime(self.end_time, date_format) -
            timedelta(hours=0, minutes=self.time_left)
        )
        return current_time

    def main_loop(self):
        if self.time_left <= 30:
            return False
        else:
            return True

    def is_meal_time(self):
        if (
            self.meal_timer <= 20 and
            self.get_current_time() > datetime.strptime('11:00', '%H:%M') and
            self.get_current_time() < datetime.strptime('21:10', '%H:%M')
        ):
            self.meal_timer = 180
            return True
        else:
            return False

    def __repr__(self):
        current_time = self.get_current_time().strftime('%H:%M')
        return (
            f'Time left: {self.time_left} mins\n'
            f'Start time: {self.start_time}\n'
            f'End time: {self.end_time}\n'
            f'Current time: {current_time}\n')
