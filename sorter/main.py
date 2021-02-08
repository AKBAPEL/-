"""
Главный модуль программы
Точка старта
"""
from sorter import loader, sorting
import click

BUBBLE = 'BUBBLE'
INSERT = 'INSERT'
SELECTION = 'SELECTION'


@click.command()
@click.option("--filename", default=None, help="Имя файла с несортированными данными")
@click.option("--algorithm", default=SELECTION, help="Алгоритм сортировки")
def sorter(filename, algorithm):
    global Sorted_data
    allowed_algorithms = [BUBBLE, INSERT, SELECTION]
    if algorithm not in allowed_algorithms:
        print('Неправильно введено имя алгоритма', allowed_algorithms)
        print("Возможные варивнты", allowed_algorithms)
        exit(1)

    print(filename, algorithm)
    if filename is None:
        unsorted_data = loader.load_from_input()
    else:
        unsorted_data = loader.load_from_file(filename)





    if algorithm == BUBBLE:
        Sorted_data = sorting.bubble_sort(unsorted_data)
    elif algorithm == INSERT:
        Sorted_data = sorting.insert_sort(unsorted_data)
    elif algorithm == SELECTION:
        Sorted_data = sorting.selection_sort(unsorted_data)
    print("Несортированный массив", *unsorted_data)
    print("Сортированный массив  ", *Sorted_data)


if __name__ == '__main__':
    sorter()
