import random

def generate_sorted(n):
    return list(range(n))

def generate_reverse_sorted(n):
    return list(range(n, 0, -1))

def generate_random(n):
    return [random.randint(0, 10000) for _ in range(n)]

def generate_almost_sorted(n, percent=10):
    arr = list(range(n))
    swaps = n * percent // 100

    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr