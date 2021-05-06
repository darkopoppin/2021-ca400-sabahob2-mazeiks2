from planner.plan import Plan


class TestPlan():

    def test_plan_init(self, test_recommended, test_user):
        plan = Plan(
                    test_recommended, (53.3471, -6.2719), '10:20', '12:35',
                    test_user['liked_categories']
        )
        assert plan.timer.time_left == 135

        assert (
            len(plan.target_categories) == len(test_user['liked_categories'])
        )
        assert plan.activity_keys != []
        assert plan.meal_keys != []

    def test_plan(self, test_recommended, test_user):
        plan = Plan(
                    test_recommended, (53.3471, -6.2719), '10:20', '12:35',
                    test_user['liked_categories']
        )
        assert plan.plan == {}

        plan.add_meal()
        assert len(plan.plan.keys()) == 1

        plan.add_activity()
        assert len(plan.plan.keys()) == 2

    def test_get_distance(self, test_recommended, test_user):
        plan = Plan(
                    test_recommended, (53.3471, -6.2719), '10:20', '12:35',
                    test_user['liked_categories']
        )

        distance, time = plan.get_graphhopper_distance(
            (53.3471, -6.2719), (53.3471, -6.2719)
        )
        assert distance == 0
        assert time == 0
