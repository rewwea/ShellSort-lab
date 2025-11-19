import time
from shell_sort import shell_sort
from insertion_sort import insertion_sort
import data_generators as gen


def run_experiment():
    sizes = [1000, 5000, 10000, 20000]

    types = {
        "sorted": gen.generate_sorted,
        "reverse": gen.generate_reverse_sorted,
        "random": gen.generate_random,
        "almost": gen.generate_almost_sorted,
    }

    for n in sizes:
        print(f"\n===== Размер массива: {n} =====")

        for name, func in types.items():
            print(f"\n-- Тип данных: {name} --")

            times = []
            comparisons_all = []
            swaps_all = []

            for _ in range(5):
                data = func(n)
                start = time.perf_counter()
                _, stats = shell_sort(data)
                end = time.perf_counter()

                times.append(end - start)
                comparisons_all.append(stats["comparisons"])
                swaps_all.append(stats["swaps"])

            median_time = sorted(times)[len(times)//2]
            avg_comparisons = sum(comparisons_all) // 5
            avg_swaps = sum(swaps_all) // 5

            print(f"Время (медиана): {median_time:.5f} сек")
            print(f"Средние сравнения: {avg_comparisons}")
            print(f"Средние перемещения: {avg_swaps}")


if __name__ == "__main__":
    run_experiment()