"""
Загруз

ка данных
"""


def str_to_int_list(raw_list):
    return [int(i) for i in raw_list.split()]


def load_from_input():
    """Получение данных через input
    :return: писок несортированных данных
    """

    while True:
        try:
            raw_list = input('Введите числа разделенные пробелом:')
            result = str_to_int_list(raw_list)
        except ValueError:
            print("Вы ввели не праильное число")
        else:
            return result


def load_from_file(filename: str) -> list:
    """
    получение данных из файла
    :param filename: имя файла
    :return: список несортированных данных
    """
    with open(filename) as file:
        raw_list = file.read()
    result = str_to_int_list(raw_list)
    return result
