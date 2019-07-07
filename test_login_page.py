import os

from dotenv import load_dotenv
import pytest

from pages.login_page import LoginPage

load_dotenv()  # loading .env file

LOGIN_PAGE_URL = 'https://courses.ultimateqa.com/users/sign_in'

VALID_EMAIL = os.getenv('VALID_EMAIL')  # retrieving valid email from .env file
VALID_PASSWORD = os.getenv('VALID_PASSWORD')  # retrieving valid password from .env file

INVALID_EMAIL = 'JohnDoe72416618@gmail.com'
INVALID_PASSWORD = 'Jsdfdsfcvx1231cxfdgb'


@pytest.mark.login
class TestLoginPage:

    def test_login_form_is_present(self, browser):
        login_page = LoginPage(browser, LOGIN_PAGE_URL)
        login_page.open()
        login_page.ensure_login_form_is_present()

    def test_login_with_valid_credentials(self, browser):
        login_page = LoginPage(browser, LOGIN_PAGE_URL)
        login_page.open()
        login_page.login(email=VALID_EMAIL, password=VALID_PASSWORD)
        login_page.ensure_login_failed_message_is_not_present()

    def test_login_with_valid_credentials_and_remember_me(self, browser):
        login_page = LoginPage(browser, LOGIN_PAGE_URL)
        login_page.open()
        login_page.login_with_remember_me(email=VALID_EMAIL, password=VALID_PASSWORD)
        login_page.ensure_login_failed_message_is_not_present()

    def test_login_with_invalid_credentials(self, browser):
        login_page = LoginPage(browser, LOGIN_PAGE_URL)
        login_page.open()
        login_page.login(email=INVALID_EMAIL, password=INVALID_PASSWORD)
        login_page.ensure_login_failed_message_is_present()

    def test_login_with_valid_email_and_invalid_password(self, browser):
        login_page = LoginPage(browser, LOGIN_PAGE_URL)
        login_page.open()
        login_page.login(email=VALID_EMAIL, password=INVALID_PASSWORD)
        login_page.ensure_login_failed_message_is_present()

    def test_login_with_invalid_email_and_valid_password(self, browser):
        login_page = LoginPage(browser, LOGIN_PAGE_URL)
        login_page.open()
        login_page.login(email=INVALID_EMAIL, password=VALID_PASSWORD)
        login_page.ensure_login_failed_message_is_present()

    def test_login_with_empty_credentials(self, browser):
        login_page = LoginPage(browser, LOGIN_PAGE_URL)
        login_page.open()
        login_page.login(email='', password='')
        login_page.ensure_login_failed_message_is_present()
