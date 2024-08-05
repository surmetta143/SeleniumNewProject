
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json

CHROME_DRIVER_PATH = "C:/Users/Jagadish/Downloads/chromedriver-win64 (2)/chromedriver-win64/chromedriver.exe"


@pytest.fixture(scope="module")
def driver():
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.close()
