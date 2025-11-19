def shell_sort(arr, reverse=False):
    """
    Сортировка Шелла.
    Возвращает: отсортированный массив и статистику (comparisons, swaps).
    """

    # Базовая проверка входных данных
    if arr is None:
        raise ValueError("Ошибка: входной массив не должен быть None")

    n = len(arr)
    gap = n // 2

    comparisons = 0
    swaps = 0

    # Основной цикл уменьшения шага
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Сравнения ключей
            while j >= gap:
                comparisons += 1

                # Учитываем reverse
                if reverse:
                    condition = arr[j - gap] < temp
                else:
                    condition = arr[j - gap] > temp

                if condition:
                    arr[j] = arr[j - gap]
                    swaps += 1
                    j -= gap
                else:
                    break

            arr[j] = temp
        gap //= 2

    return arr, {"comparisons": comparisons, "swaps": swaps}