from planner.my_time import Time


class TestTime():

    def test_duration(self):
        time = Time('10:20', '12:35')
        assert time.time_left == 135

    def test_decriment(self):
        time = Time('10:20', '12:35')

        time.decriment_time_left('activity')
        expected = 135 - 45
        assert time.time_left == expected

        time.decriment_time_left('meal')
        expected -= 50
        assert time.time_left == expected

        time.decriment_time_left('walk', 10)
        expected -= 10
        assert time.time_left == expected

    def test_current_time(self):
        time = Time('10:20', '12:35')
        assert time.get_current_time().strftime('%H:%M') == '10:20'

    def test_is_meal_time(self):
        time = Time('10:20', '12:35')
        assert time.is_meal_time() is False

        time.decriment_time_left('activity')
        assert time.is_meal_time() is False

        for i in range(0, 6):
            time.decriment_time_left('activity')
        assert time.is_meal_time() is True

    def test_main_loop(self):
        time = Time('10:20', '12:35')
        assert time.main_loop() is True

        for i in range(0, int(time.time_left / 45)):
            time.decriment_time_left('activity')
        assert time.main_loop() is False
