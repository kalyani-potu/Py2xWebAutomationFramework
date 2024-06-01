
# Page Class

# Page Locators
# Page Actions
# WebDriver Init
# Custom Functions
# No assertions(in Page Object Class)

from seleniumpagefactory.Pagefactory import PageFactory

class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'username' : ('CSS', "#login-username"),
        'password' : ('NAME', "password"),
        'submit_button' : ('XPATH', "//button[@id='js-login-btn']"),
        # forgot_password_button = (By.XPATH, "//button[normalize-space()='Forgot Password?']")
        'error_message' : ('CSS', "#js-notification-box-msg")
    }


    # Page Action - Main Action
    def login_to_vwo(self, usr,pwd):
        self.username.set_text(usr)
        self.password.set_text(pwd)
        self.submit_button.click_button()

    def error_message(self):
        return self.error_message.get_text()

    # https://selenium-page-factory.readthedocs.io/en/latest/
    # Extended WebElements Methods
    # set_text	get_text
    # clear_text	click_button
    # double_click	get_list_item_count
    # select_element_by_text	select_element_by_index
    # select_element_by_value	get_all_list_item
    # get_list_selected_item	highlight
    # is_Enabled	is_Checked
    # getAttribute	hover
    # visibility_of_element_located	invisibility_of_element_located
    # element_to_be_clickable	execute_script
    # context_click	text_to_be_present_in_element
    # click_and_hold	release




