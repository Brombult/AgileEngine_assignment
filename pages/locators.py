from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, 'user_email')
    PASSWORD_FIELD = (By.ID, 'user_password')
    REMEMBER_ME_CHECKBOX = (By.ID, 'user_remember_me')
    FORGOT_PASSWORD_LINK = (By.CLASS_NAME, 'forgot-password')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'input[value="Sign in"]')
    LOGIN_FAILED_MESSAGE = (By.CSS_SELECTOR, 'div[data-message="Invalid Email or password."]')


class MainPageLocators:
    SIGN_IN_SUCCESSFULLY = (By.CSS_SELECTOR, 'div[data-message="Signed in successfully."]')
