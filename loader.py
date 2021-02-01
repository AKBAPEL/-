"""
Загруз

ка данных
"""


def load_from_input():
    """Получение данных через inpuе
    :return: писок несортированных данных
    """

    while True:
        try:
            raw_list = input('Введите числа разделенные пробелом:')
            result = [int(i) for i in raw_list.split()]
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
    ...