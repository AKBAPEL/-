"""
Тесты
"""
import sorting
import pytest


DEFAULT_LIST = [3, 1, 4, 5, 22, 8, 9, 6, 7]
EMPTY_LIST = []
NEGATIVE_LIST = [-1, 6, 22, 8, -9]
NONVALID_LIST = [3, -1, 4, 5, '-2', 8, 9, 6, 7]






@pytest.mark.parametrize("test_list", [DEFAULT_LIST, NEGATIVE_LIST, EMPTY_LIST])
@pytest.mark.parametrize("test_func", [sorting.bubble_sort, sorting.selection_sort, sorting.insert_sort])


def test_all(test_list,test_func):
    result = test_func(test_list)
    assert result == sorted(test_list)



