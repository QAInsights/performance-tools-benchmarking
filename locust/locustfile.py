"""locust file"""
import math
from typing import Generator

from locust import HttpUser, task, constant, LoadTestShape


class WebsiteUser(HttpUser):
    """users container"""

    wait_time = constant(1)
    host = "https://petclinic.ycrash.io/"
    data: Generator

    @task(1)
    def simple_get(self):
        """performs get"""
        self.client.get("")


class StepLoadShape(LoadTestShape):
    """
    A step load shape


    Keyword arguments:

        step_time -- Time between steps
        step_load -- User increase amount at each step
        spawn_rate -- Users to stop/start per second at every step
        time_limit -- Time limit in seconds

    """

    step_time = 10
    step_load = 50
    spawn_rate = 50
    time_limit = 50

    def tick(self):
        run_time = self.get_run_time()

        if run_time > self.time_limit:
            return None

        current_step = math.floor(run_time / self.step_time) + 1
        return (current_step * self.step_load, self.spawn_rate)
