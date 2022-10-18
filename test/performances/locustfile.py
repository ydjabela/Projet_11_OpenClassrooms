from locust import HttpUser, task


class PerfTest(HttpUser):
    """
    Performance tests on main urls
    """

    @task
    def perf_index(self):
        self.client.get("/")

    @task
    def perf_logout(self):
        self.client.get("/logout")

    @task
    def perf_points(self):
        self.client.get("/clubs")

    @task
    def perf_login(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task
    def perf_book(self):
        self.client.get("/book/Spring%20Festival/Simply%20Lift")

    @task
    def perf_purchase(self):
        self.client.post("/purchasePlaces", data={"competition": "Competition Locust", "club": "Club Locust", "places": 1})
