"""locust file"""
from locust import FastHttpUser, task, between


class WebsiteUser(FastHttpUser):
    """users container"""

    wait_time = between(1, 5)
    host = "https://petclinic.ycrash.io/"

    @task(1)
    def simple_get(self):
        """performs get"""
        self.client.get("")
