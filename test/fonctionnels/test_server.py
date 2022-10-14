from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


class TestFunctional:

    def check_places(self, driver, places, message):
        href = "/book/Spring%20Festival/Simply%20Lift"
        driver.find_element(by=By.XPATH, value=f"//a[@href='{href}']").click()
        assert driver.find_element(By.TAG_NAME, "h2").text == "Spring Festival"

        # Enter  number of places  and  click Book
        driver.find_element(By.NAME, "places").send_keys(places, Keys.ENTER)
        assert driver.find_element(By.TAG_NAME, "li").text == message

    def test_server(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # Open localhost
        driver.get("http://127.0.0.1:5000")
        assert "GUDLFT Registration" in driver.title
        assert driver.find_element(By.TAG_NAME, "h1").text == "Welcome to the GUDLFT Registration Portal!"

        # Enter  email and  click Enter
        email = "john@simplylift.co"
        driver.find_element(By.NAME, "email").send_keys(email, Keys.ENTER)
        assert driver.find_element(By.TAG_NAME, "h2").text == "Welcome, john@simplylift.co"

        self.check_places(driver=driver, places=2, message="Great-booking complete!")

        self.check_places(driver=driver, places=14, message="the number of places need to be under to 12")

        self.check_places(driver=driver, places=-2, message="the number of places need to be not negative")

        self.check_places(driver=driver, places=5, message="Not enough points")

        self.check_places(driver=driver, places=7, message="Not enough points")

        # logout
        href = "/logout"
        driver.find_element(by=By.XPATH, value=f"//a[@href='{href}']").click()
        assert driver.find_element(By.TAG_NAME, "h1").text == "Welcome to the GUDLFT Registration Portal!"





