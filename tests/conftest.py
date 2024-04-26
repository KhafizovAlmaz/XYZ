from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def chrome():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                              options=options)
    yield driver
    driver.quit()
