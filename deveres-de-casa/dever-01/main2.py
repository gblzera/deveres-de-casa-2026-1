import random
import time

# sizes 
SIZES = [1_000, 5_000, 10_000, 20_000, 50_000]


def insertion_sort(data):
    """Sorts a list in-place using insertion sort algorithm."""
    n = len(data)

    for i in range(1, n):
        key = data[i]
        j = i - 1

        # shift elements that are greater than key to the right
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


def run_benchmark():
    """Runs the full benchmark for all sizes and prints results."""
    random.seed(42)  # fixed seed so both algorithms get the same data

    print("=" * 70)
    print("  insertion sort O(n*n)  x  timsort O(n log n)")
    print("=" * 70)
    print(f"  {'n':>10}  |  {'insertion sort':>16}  |  {'timsort':>16}  |  {'speedup':>8}")
    print("-" * 70)

    for size in SIZES:
        # generate a fresh random list for this size
        original = [random.randint(0, 1_000_000) for _ in range(size)]

        # insertion sort
        copy_1 = original.copy()
        start = time.perf_counter()
        insertion_sort(copy_1)
        time_insertion = time.perf_counter() - start

        # timsort (built-in)
        copy_2 = original.copy()
        start = time.perf_counter()
        sorted(copy_2)
        time_timsort = time.perf_counter() - start

        # how many times faster 
        speedup = time_insertion / time_timsort if time_timsort > 0 else 0

        print(
            f"  {size:>10,}  |  {time_insertion:>14.6f} s  |"
            f"  {time_timsort:>14.6f} s  |  {speedup:>6.1f}x"
        )

    print("-" * 70)
    print("  * using time.perf_counter() for precision")
    print("  * same random seed (42) for reproducibility")
    print("=" * 70)


if __name__ == "__main__":
    run_benchmark()