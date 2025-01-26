from locust import HttpUser, task, between

class ConfitureUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_confiture(self):
        self.client.get("/label?q=confiture")