from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    apt_btn = (By.ID, "btn-make-appointment")

    # Page Locators
    def get_apt_btn(self):
        return self.driver.find_element(*HomePage.apt_btn)

    #Page Actions
    def click_make_apt(self):
        self.get_apt_btn().click()


