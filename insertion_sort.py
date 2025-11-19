def insertion_sort(arr, reverse=False):
    """
    Классическая сортировка вставками.
    Возвращает: отсортированный массив и статистику.
    """

    if arr is None:
        raise ValueError("Ошибка: входной массив не должен быть None")

    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if reverse:
                condition = arr[j] < key
            else:
                condition = arr[j] > key

            if condition:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return arr, {"comparisons": comparisons, "swaps": swaps}