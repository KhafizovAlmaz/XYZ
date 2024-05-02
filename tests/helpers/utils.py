import datetime
import allure


# Реализация вычисления числа Фибоначчи
def fibonacci(n):
    if n <= 0:
        return "Неверное значение n"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


current_day = datetime.datetime.now().day
amount = fibonacci(current_day + 1)


def attach_csv_file(file_name=''):
    # Прикладываем файл к отчету
    with open(file_name, 'rb') as file:
        allure.attach(file.read(), name=file_name, attachment_type=allure.attachment_type.CSV)
