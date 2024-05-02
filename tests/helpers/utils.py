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
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        return fib_sequence[-1]


current_day = datetime.datetime.now().day
amount = fibonacci(current_day + 1)


def attach_csv_file(file_name=''):
    # Прикладываем файл к отчету
    with open(file_name, 'rb') as file:
        allure.attach(file.read(), name=file_name, attachment_type=allure.attachment_type.CSV)
