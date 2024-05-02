# XYZ bank

Автономный режим легко объединяет все компоненты Grid в один. Запуск Grid в автономном режиме дает вам полнофункциональный Grid с помощью одной команды в рамках одного процесса. Автономный режим может работать только на одной машине.

Автономный режим также является самым простым режимом для развертывания Selenium Grid. По умолчанию сервер будет прослушивать RemoteWebDriverзапросы на http://localhost:4444 . По умолчанию сервер обнаружит доступные драйверы, которые он может использовать в системе PATH.

Запуск Selenium Grid:
```sh
java -jar selenium-server-4.19.1.jar standalone
```

После успешного запуска Grid в автономном режиме укажите для тестов WebDriver адрес http://localhost:4444 .

Установка зависимостей:

```commandline
pip install -r requirements.txt
```

Запуск тестов: 

```commandline
pytest -v -s --alluredir results
```

Allure отчеты:

```commandline
allure serve results
```