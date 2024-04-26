from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
import datetime
import allure


class BasePage:

    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url
        self.current_day = datetime.datetime.now().day
        self.amount = self.fibonacci(self.current_day + 1)

    def start_script(self):
        with allure.step('Открытие страницы'):
            self.open()

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5) -> WebElement:
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5) -> WebElement:
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def select_option(self, locator, value):
        select = Select(self.driver.find_element(*locator))
        select.select_by_value(*value)

    def check_text(self, required_text, locator, timeout=5, error_msg="Текст не соответствует ожидаемому"):
        real_text = self.element_is_visible(locator, timeout=timeout).text
        assert real_text == required_text, f"{error_msg}, фактический результат - {real_text}," \
                                                f" ожидаемый резуьтат - {required_text}"

    @staticmethod
    def fibonacci(n):
        if n <= 0:
            return "Неверное значение n"
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            fib_sequence = [0, 1]
            for i in range(2, n):
                next_fib = fib_sequence[-1] + fib_sequence[-2]
                fib_sequence.append(next_fib)
            return fib_sequence[-1]

    @staticmethod
    def attach_csv_file(file_name=''):
        # Прикладываем файл к отчету
        with open(file_name, 'rb') as file:
            allure.attach(file.read(), name=file_name, attachment_type=allure.attachment_type.CSV)
