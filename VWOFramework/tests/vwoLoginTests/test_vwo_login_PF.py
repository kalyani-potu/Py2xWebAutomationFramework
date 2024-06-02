import time

import allure
import pytest
from selenium import webdriver
from tests.pageObjects.loginPage_PF import LoginPage
from allure_commons.types import AttachmentType
#from dotenv import load_dotenv

@allure.epic("VWO App")
@allure.feature("Login Test")
class TestVWOLogin:
    #load_dotenv()
    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwologin_negative(self,setup):
        driver = setup
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.login_to_vwo(usr=self.username, pwd="123")
        time.sleep(5)
        if "Dashboard" not in driver.title:
            allure.attach(driver.get_screenshot_as_png(), name="VWO screenshot", attachment_type=AttachmentType.PNG)
        time.sleep(5)

    @pytest.mark.usefixtures("setup")
    @pytest.mark.smoke
    def test_vwologin_positive(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.login_to_vwo(usr=self.username, pwd=self.password)
        time.sleep(5)
        assert "Dashboard" in driver.title
        time.sleep(5)


