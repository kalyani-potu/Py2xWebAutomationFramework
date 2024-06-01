from selenium.webdriver.common.by import By


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    appt_confrmtn_head = (By.XPATH, "//div[@class='col-xs-12 text-center']/h2")
    facility = (By.XPATH, "//div/p[@id='facility']")
    hospital_readmission = (By.XPATH, "//p[@id='hospital_readmission']")
    program = (By.XPATH, "//p[@id='program']")
    visit_date = (By.XPATH, "//p[@id='visit_date']")
    comment = (By.XPATH, "//p[@id='comment']")

    # page locators
    def get_appt_confrmtn_head(self):
        return self.driver.find_element(*ConfirmationPage.appt_confrmtn_head).text

    def get_facility_text(self):
        return self.driver.find_element(*ConfirmationPage.facility).text

    def get_hospital_readmission_text(self):
        return self.driver.find_element(*ConfirmationPage.hospital_readmission).text

    def get_program_text(self):
        return self.driver.find_element(*ConfirmationPage.program).text

    def get_visit_date_text(self):
        return self.driver.find_element(*ConfirmationPage.visit_date).text

    def get_comment_text(self):
        return self.driver.find_element(*ConfirmationPage.comment).text
