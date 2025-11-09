import random
from sort_algorithms.qsort import qsort


def test_empty_list():
    assert qsort([]) == []


def test_single_element():
    assert qsort([5]) == [5]


def test_already_sorted():
    assert qsort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    assert qsort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_unsorted_list():
    data = [64, 34, 25, 12, 22, 11, 90]
    assert qsort(data) == sorted(data)


def test_with_duplicates():
    data = [3, 1, 2, 3, 1]
    assert qsort(data) == [1, 1, 2, 3, 3]


def test_negative_numbers():
    data = [0, -1, 3, -2, 2]
    assert qsort(data) == [-2, -1, 0, 2, 3]


def test_original_unchanged():
    data = [3, 2, 1]
    assert qsort(data) == [1, 2, 3]


def test_random_elements():
    data = [random.randint(-1000, 1000) for _ in range(1000)]
    result = qsort(data)
    assert result == sorted(data)