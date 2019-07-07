from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):

    def confirm_main_page_is_open(self):
        assert 'courses.ultimateqa' in self.browser.current_url, 'not on main page'

    def confirm_that_sign_in_successful_message_is_displayed(self):
        assert self.is_element_present(*MainPageLocators.SIGN_IN_SUCCESSFULLY_MESSAGE), \
            'no "Signed in successfully" message is displayed'
