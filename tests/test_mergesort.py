import random
from sort_algorithms.mergesort import merge_sort


def test_empty_list():
    assert merge_sort([]) == []


def test_single_element():
    assert merge_sort([5]) == [5]


def test_already_sorted():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_unsorted_list():
    data = [64, 34, 25, 12, 22, 11, 90]
    assert merge_sort(data) == sorted(data)


def test_with_duplicates():
    data = [3, 1, 2, 3, 1]
    assert merge_sort(data) == [1, 1, 2, 3, 3]


def test_negative_numbers():
    data = [0, -1, 3, -2, 2]
    assert merge_sort(data) == [-2, -1, 0, 2, 3]


def test_original_unchanged():
    data = [3, 2, 1]
    assert merge_sort(data) == [1, 2, 3]


def test_random_elements():
    data = [random.randint(-1000, 1000) for _ in range(1000)]
    result = merge_sort(data)
    assert result == sorted(data)