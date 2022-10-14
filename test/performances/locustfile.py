from locust import HttpUser, task, between

class TestPerformance(HttpUser):
    @task
    def home(self):
        self.client.get("/")



class WebsiteUser(HttpUser):
    task_set = TestPerformance
    min_wait = 5000
    max_wait = 9000
    host="http://127.0.0.1:5000"
