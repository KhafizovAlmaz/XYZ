import csv
import allure
from locators.global_sqa_locators import GlobalSqaLocators
from pages.base_page import BasePage


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
            self.element_is_visible(self.locators.AMOUNT_INPUT).send_keys(self.amount)
            self.element_is_clickable(self.locators.AMOUNT_SUBMIT).click()
            self.check_text('Deposit Successful', self.locators.OPERATION_TEXT)

    def withdrawl(self):
        with allure.step('Cписание со счета (Withdrawl)'):
            self.element_is_clickable(self.locators.WITHDRAWL_BTN).click()
            self.element_is_visible(self.locators.AMOUNT_INPUT).send_keys(self.amount)
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
            assert credit_trnsctn == 'Credit' and credit_amnt == self.amount, 'Транзакция credit отсутсвует'
            assert debit_trnsctn == 'Debit' and debit_amnt == self.amount, 'Транзакция debit отсутсвует'

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
                writer.writerow([cr_date_time, self.amount, credit_trnsctn])
                writer.writerow([db_date_time, self.amount, debit_trnsctn])
            self.element_is_clickable(self.locators.RESET_BTN).click()
            self.attach_csv_file('transactions.csv')
