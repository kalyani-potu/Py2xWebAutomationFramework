from selenium.webdriver.common.by import By


class AppointmentPage:
    def __init__(self, driver):
        self.driver = driver

    facility = (By.XPATH, "//select[@id = 'combo_facility']/option[3]")
    check_box = (By.ID, "chk_hospotal_readmission")
    health_care_rdbtn = (By.ID, "radio_program_none")
    visit_date = (By.ID, "txt_visit_date")
    comment = (By.ID, "txt_comment")
    book_appt = (By.ID, "btn-book-appointment")

    # Page locators
    def get_facility(self):
        return self.driver.find_element(*AppointmentPage.facility)

    def get_check_box(self):
        return self.driver.find_element(*AppointmentPage.check_box)

    def get_health_care_rdbtn(self):
        return self.driver.find_element(*AppointmentPage.health_care_rdbtn)

    def get_visit_date(self):
        return self.driver.find_element(*AppointmentPage.visit_date)

    def get_comment(self):
        return self.driver.find_element(*AppointmentPage.comment)

    def get_book_appt(self):
        return self.driver.find_element(*AppointmentPage.book_appt)

    def book_appointment(self, date, comment):
        self.get_facility().click()
        self.get_check_box().click()
        self.get_health_care_rdbtn().click()
        self.get_visit_date().send_keys(date)
        self.get_comment().send_keys(comment)
        self.get_book_appt().click()