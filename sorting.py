"""
Функции сортировки
"""
def _validate(input_lst):
    for e in input_lst:
        if not isinstance(e, int):
            raise RuntimeError(f"Элемент '{e}' не являяется числом")


def bubble_sort(unsortred_data: list) -> list:
    """Сортировка методом пузырька
    :param unsortred_data Несортированные данные
    """
    _validate(unsortred_data)
    data = unsortred_data [:]
    for element in range(len(data) - 1, 0 , -1):
        for current in range(0, element):
            if data[current] > data[current + 1]:
                data[current], data[current + 1] = (
                        data[current + 1],  data[current])
    return data


def insert_sort(unsortred_data: list) -> list:
    """Сортировка методом вставки
    :param unsortred_data Несортированные данные

    """
    _validate(unsortred_data)
    data = unsortred_data[:]
    for i in range(1, len(data)):
        current = data[i]
        j = i - 1
        while data[i] < data[j]  and j>= 0:
            data[i], data[j] = data[j], data[i]
            j = j - 1
        j = j + 1
        data[j] = current

    return data


def selection_sort(unsortred_data: list) -> list:
     """Сортировка методом выбора
     :param unsortred_data Несортированные данные

     """
     _validate(unsortred_data)
     data = unsortred_data[:]
     for i in range(len(data)-1):
         for j in range(i + 1, len(data)):
             if data[i] > data[j]:
                 data[i], data[j] = data[j], data[i]
     return data
