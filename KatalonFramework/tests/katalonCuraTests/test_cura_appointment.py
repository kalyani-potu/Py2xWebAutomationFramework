import time

import allure
import pytest
from selenium import webdriver
from KatalonFramework.tests.pageObjects.curaHomePage import HomePage
from KatalonFramework.tests.pageObjects.curaLoginPage import LoginPage
from KatalonFramework.tests.pageObjects.curaAppointmentPage import AppointmentPage
from KatalonFramework.tests.pageObjects.curaConfirmationPage import ConfirmationPage
from allure_commons.types import AttachmentType

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    return driver

@allure.epic("Cura Appointment Test")
@allure.feature("TC#1 - Cura Appointment Positive Test")
def test_make_appointment(setup):
    driver = setup
    homepage_obj = HomePage(driver)
    homepage_obj.click_make_apt()
    loginpage_obj = LoginPage(driver)
    loginpage_obj.login_cura(usr="John Doe", pwd="ThisIsNotAPassword")
    time.sleep(3)
    appointment_obj = AppointmentPage(driver)
    appointment_obj.book_appointment(date="01/06/2024", comment="BBB comment")
    time.sleep(3)
    confirmation_obj = ConfirmationPage(driver)
    assert confirmation_obj.get_appt_confrmtn_head() == "Appointment Confirmation"
    assert confirmation_obj.get_facility_text() == "Seoul CURA Healthcare Center"
    assert confirmation_obj.get_hospital_readmission_text() == "Yes"
    assert confirmation_obj.get_program_text() == "None"
    assert confirmation_obj.get_visit_date_text() == "01/06/2024"
    assert confirmation_obj.get_comment_text() == "BBB comment"
    allure.attach(driver.get_screenshot_as_png(), name="Cura Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(3)

