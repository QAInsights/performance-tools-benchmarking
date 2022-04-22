"""locust file"""
from typing import Generator

from locust import HttpUser, task, constant_pacing, LoadTestShape


class WebsiteUser(HttpUser):
    """users container"""

    wait_time = constant_pacing(1)
    host = "https://petclinic.ycrash.io/"
    data: Generator

    @task(1)
    def simple_get(self):
        """performs get"""
        self.client.get("")


class StagesShape(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.

    Keyword arguments:

        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage

        stop_at_end -- Can be set to stop once all stages have run.
    """

    total_steps = 20
    rate = 50
    stages = [
        {"duration": 30 * i, "users": 50 * i, "spawn_rate": 50}
        for i in range(1, total_steps + 1)
    ]
    stages.append(
        {"duration": 30 * total_steps, "users": 50 * total_steps, "spawn_rate": 50}
    )

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data


# class StepLoadShape(LoadTestShape):
#     """
#     A step load shape


#     Keyword arguments:

#         step_time -- Time between steps
#         step_load -- User increase amount at each step
#         spawn_rate -- Users to stop/start per second at every step
#         time_limit -- Time limit in seconds

#     """

#     step_time = 30
#     step_load = 50
#     spawn_rate = 50
#     time_limit = 660

#     def tick(self):
#         run_time = self.get_run_time()

#         if run_time > self.time_limit:
#             return None

#         current_step = math.floor(run_time / self.step_time) + 1
#         return (current_step * self.step_load, self.spawn_rate)
