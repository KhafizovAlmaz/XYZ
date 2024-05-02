import allure
from locators.global_sqa_locators import GlobalSqaLocators
from pages.base_page import BasePage
from tests.helpers.utils import amount


class GlobalSqaPage(BasePage):
    locators = GlobalSqaLocators()

    def authorization(self):
        with allure.step('Авторизация в сервисе по аккаунтом Harry Potter'):
            self.element_is_clickable(self.locators.CUSTOM_LOGIN).click()
            self.select_option(self.locators.USER_LIST, "2")
            self.element_is_clickable(self.locators.SUBMIT_BTN).click()
            self.check_text('Harry Potter', self.locators.USER_NAME)

    def deposit(self):
        with allure.step('Пополнение счета (Deposit)'):
            self.element_is_clickable(self.locators.DEPOSIT_BTN).click()
            self.element_is_visible(self.locators.AMOUNT_INPUT).send_keys(amount)
            self.element_is_clickable(self.locators.AMOUNT_SUBMIT).click()
            self.check_text('Deposit Successful', self.locators.OPERATION_TEXT)

    def withdrawl(self):
        with allure.step('Cписание со счета (Withdrawl)'):
            self.element_is_clickable(self.locators.WITHDRAWL_BTN).click()
            self.element_is_visible(self.locators.AMOUNT_INPUT).send_keys(amount)
            self.element_is_clickable(self.locators.AMOUNT_SUBMIT).click()
            self.check_text('Transaction successful', self.locators.OPERATION_TEXT)

    def check_balance(self):
        with allure.step('Проверка баланса равным нулю'):
            self.check_text('0', self.locators.BALANCE_NUM)

    def check_transactions(self):
        with allure.step('Проверка наличия транзакций'):
            self.element_is_clickable(self.locators.TRANSACTIONS_PAGE_BTN).click()
            credit_trnsctn = self.element_is_visible(self.locators.TRANS_CREDIT_TITLE, timeout=5).text
            credit_amnt = self.element_is_visible(self.locators.TRANS_CREDIT_AMOUNT, timeout=5).text
            debit_trnsctn = self.element_is_visible(self.locators.TRANS_DEBIT_TITLE, timeout=5).text
            debit_amnt = self.element_is_visible(self.locators.TRANS_DEBIT_AMOUNT, timeout=5).text
            assert credit_trnsctn == 'Credit' and credit_amnt == amount, 'Транзакция credit отсутсвует'
            assert debit_trnsctn == 'Debit' and debit_amnt == amount, 'Транзакция debit отсутсвует'
