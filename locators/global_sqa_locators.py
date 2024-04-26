from selenium.webdriver.common.by import By


class GlobalSqaLocators:
    CUSTOM_LOGIN = (By.CSS_SELECTOR, 'button[ng-click="customer()"]')
    USER_LIST = (By.ID, 'userSelect')
    SUBMIT_BTN = (By.CLASS_NAME, 'btn-default')
    USER_NAME = (By.CLASS_NAME, 'fontBig')

    DEPOSIT_BTN = (By.CSS_SELECTOR, 'button[ng-class*="Class2"]')
    AMOUNT_INPUT = (By.CSS_SELECTOR, 'input[ng-model="amount"]')
    AMOUNT_SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"]')
    OPERATION_TEXT = (By.CLASS_NAME, 'error')
    WITHDRAWL_BTN = (By.CSS_SELECTOR, 'button[ng-class*="Class3"]')
    BALANCE_NUM = (By.CSS_SELECTOR, 'div.center strong:nth-child(2)')

    TRANSACTIONS_PAGE_BTN = (By.CSS_SELECTOR, 'button[ng-class="btnClass1"]')
    TRANS_CREDIT_AMOUNT = (By.CSS_SELECTOR, '#anchor0 td:nth-child(2)')
    TRANS_CREDIT_TITLE = (By.CSS_SELECTOR, '#anchor0 td:nth-child(3)')
    TRANS_DEBIT_AMOUNT = (By.CSS_SELECTOR, '#anchor1 td:nth-child(2)')
    TRANS_DEBIT_TITLE = (By.CSS_SELECTOR, '#anchor1 td:nth-child(3)')
    RESET_BTN = (By.CSS_SELECTOR, 'button[ng-click="reset()"]')
    CREDIT_DATE_TIME = (By.CSS_SELECTOR, '#anchor0 td:nth-child(1)')
    DEBIT_DATE_TIME = (By.CSS_SELECTOR, '#anchor1 td:nth-child(1)')
