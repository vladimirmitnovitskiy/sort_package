def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # выбираем опорный элемент
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return qsort(left) + middle + qsort(right)