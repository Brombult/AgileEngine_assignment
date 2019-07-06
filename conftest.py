import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
