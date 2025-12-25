
class AccountInfoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def fill_account_info(self, user_data):
        self.type(self.locators.NAME_INPUT, user_data['name'])
        self.type(self.locators.EMAIL_INPUT, user_data['email'])
        self.type(self.locators.PASSWORD_INPUT, user_data['password'])
        self.click(self.locators.SIGNUP_BUTTON)
