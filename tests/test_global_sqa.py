from pages.global_sqa_page import GlobalSqaPage
import allure


class TestGlobalSqa:
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    @allure.feature('Проверка сервиса XYZ Bank')
    @allure.story('Проверка работоспособности транзацкий ')
    def test_main(self, chrome):
        service = GlobalSqaPage(driver=chrome, url=self.url)
        service.start_script()
        service.authorization()
        service.deposit()
        service.withdrawl()
        service.check_balance()
        service.check_transactions()
        service.csv_generate()
