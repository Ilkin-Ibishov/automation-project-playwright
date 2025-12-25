import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.config import Config
from utils.helpers import get_unique_email
from pages.base_page import BasePage
from pages.register_page import RegisterPage

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": Config.HEADLESS,
        "slow_mo": 50,
    }

@pytest.fixture
def base_page(page):
    return BasePage(page)

@pytest.fixture
def register_page(page):
    return RegisterPage(page)

@pytest.fixture
def unique_email():
    return get_unique_email()

@pytest.fixture
def new_user_data(unique_email):
    return {
        "name": "Test User",
        "email": unique_email,
        "password": "Test@123",
    }


@pytest.fixture
def on_login_page(base_page):
    base_page.go_to(Config.LOGIN_URL)
    return base_page

@pytest.fixture
def on_enter_account_info_page(base_page, register_page, unique_email):
    base_page.go_to(Config.SIGNUP_URL)
    register_page.start_signup("Test User", unique_email)
    return register_page