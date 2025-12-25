from utils.config import Config
from data.locators import REGISTRATION_TITLE, EMAIL_EXISTS_ERROR
from data.constants import EXISTING_EMAIL

def test_register_with_unique_email(on_login_page, register_page, unique_email):
    register_page.start_signup("Test User", unique_email)
    on_login_page.wait_for(REGISTRATION_TITLE)
    assert on_login_page.get_url() == Config.SIGNUP_URL
    assert on_login_page.is_visible(REGISTRATION_TITLE)

def test_register_with_existing_email(on_login_page, register_page):
    register_page.start_signup("Test User", EXISTING_EMAIL)
    on_login_page.wait_for(EMAIL_EXISTS_ERROR)
    assert on_login_page.is_visible(EMAIL_EXISTS_ERROR)


# def test_register_enter_account_info()