from selenium import webdriver
from selenium.webdriver import Chrome
import pytest

# WebDriver fixture example

import os # importing os module for environment variables
from dotenv import load_dotenv # importing necessary functions from dotenv library
load_dotenv() # loading variables from .env file


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    username = os.getenv("VWO_USERNAME") #getting username from .env, # accessing variable value
    password = os.getenv("VWO_PASSWORD")
    base_url = os.getenv("BASE_URL")

    request.cls.driver = driver
    request.cls.username = username #we can use same variable name(username) as username directly in test
    request.cls.password = password
    request.cls.base_url = base_url

    yield driver #yield is same as return
    driver.quit()

