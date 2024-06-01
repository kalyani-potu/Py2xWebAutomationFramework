from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    username = (By.ID, "txt-username")
    password = (By.ID, "txt-password")
    login_btn = (By.ID, "btn-login")

    #page locators
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_loginbtn(self):
        return self.driver.find_element(*LoginPage.login_btn)

    #page actions
    def login_cura(self, usr, pwd):
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.get_loginbtn().click()