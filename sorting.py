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
    for element in range(len(unsortred_data) - 1, 0 , -1):
        for current in range(0, element):
            if data[current] > data[current + 1]:
                data[current], data[current + 1] = (
                        data[current + 1],  data[current])
    return data

def insert_sort(unsortred_data: list) -> list:
    """Сортировка методом вставки
    :param unsortred_data Несортированные данные

    """

def selection_sort(unsortred_data: list) -> list:
     """Сортировка методом выбора
     :param unsortred_data Несортированные данные

     """