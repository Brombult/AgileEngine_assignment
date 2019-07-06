from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def login(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON).click()

    def login_with_remember_me(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX).click()
        self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON).click()

    def ensure_login_failed_message_is_present(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FAILED_MESSAGE), 'no "login failed message"'

    def ensure_login_failed_message_is_not_present(self):
        assert self.is_not_element_present(*LoginPageLocators.LOGIN_FAILED_MESSAGE), '"login failed message" is present'

    def ensure_login_form_is_present(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FIELD), 'no "email" field'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD), 'no "password" field'
        assert self.is_element_present(*LoginPageLocators.REMEMBER_ME_CHECKBOX), 'no "remember me" checkbox'
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD_LINK), 'no "forgot password" link'
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_BUTTON), 'no "sign in" button'
