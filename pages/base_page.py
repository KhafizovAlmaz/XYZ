from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from locators.global_sqa_locators import GlobalSqaLocators
from tests.helpers.utils import amount, attach_csv_file
import allure
import csv


class BasePage:
    locators = GlobalSqaLocators()

    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url

    def start_script(self):
        with allure.step('Открытие страницы'):
            self.open()

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5) -> WebElement:
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5) -> WebElement:
        return Wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def select_option(self, locator, value):
        select = Select(self.driver.find_element(*locator))
        select.select_by_value(*value)

    def check_text(self, required_text, locator, timeout=5, error_msg="Текст не соответствует ожидаемому"):
        real_text = self.element_is_visible(locator, timeout=timeout).text
        assert real_text == required_text, (f'{error_msg}, фактический результат - {real_text},'
                                            f' ожидаемый резуьтат - {required_text}')

    def csv_generate(self):
        with allure.step('Генерация csv файла'):
            credit_trnsctn = self.element_is_visible(self.locators.TRANS_CREDIT_TITLE, timeout=5).text
            cr_date = self.element_is_visible(self.locators.CREDIT_DATE_TIME, timeout=5).text
            cr_date_time = ("{0} {1} {2} {3} {4}".format(cr_date.split(",")[0].split()[1], cr_date.split()[0],
                                                         cr_date.split()[2], cr_date.split()[3], cr_date.split()[4]))
            debit_trnsctn = self.element_is_visible(self.locators.TRANS_DEBIT_TITLE, timeout=5).text
            db_date = self.element_is_visible(self.locators.DEBIT_DATE_TIME, timeout=5).text
            db_date_time = ("{0} {1} {2} {3} {4}".format(db_date.split(",")[0].split()[1], db_date.split()[0],
                                                         db_date.split()[2], db_date.split()[3], db_date.split()[4]))
            # Открываем файл для записи
            with open('transactions.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                # Записываем данные в строки
                writer.writerow([cr_date_time, amount, credit_trnsctn])
                writer.writerow([db_date_time, amount, debit_trnsctn])
            self.element_is_clickable(self.locators.RESET_BTN).click()
            attach_csv_file('transactions.csv')
