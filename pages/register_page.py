from pages.base_page import BasePage
from data.locators import *

class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def start_signup(self, name: str, email: str):
        self.type(SIGNUP_NAME, name)
        self.type(SIGNUP_EMAIL, email)
        self.click(SIGNUP_BUTTON)