import time
import random
from typing import Final

""""
Sorting Algorithm Benchmark: Insertion Sort O(n*n) vs Timsort O(n log n).

This module empirically compares the execution time of a manual Insertion Sort
implementation against Python's built-in sorted() (Timsort) across increasing
input sizes, identifying the practical "breaking point" where asymptotic
complexity becomes visible.

PEP 8 / PEP 257 Compliant
"""

# contants
INPUT_SIZES: Final[list[int]] = [1_000, 5_000, 10_000, 20_000, 50_000]
RANDOM_LOWER_BOUND: Final[int] = 0
RANDOM_UPPER_BOUND: Final[int] = 1_000_000
RANDOM_SEED: Final[int] = 42
SEPARATOR: Final[str] = '=' * 72
SUB_SEPARATOR: Final[str] = '-' * 72

# sorting algorithms
def insertion_sort(data: list[int]) -> list[int]:
    """
    Sort a list of integers in ascending order using Insertion Sort.

    The algorithm iterates through the list, shifting each element into its
    correct position within the already-sorted prefix. This implementation
    uses an optimised inner loop with a single assignment per shift instead
    of repeated swaps, reducing constant-factor overhead.

    Time Complexity:
        Best:    O(n)   — already sorted input
        Average: O(n*n)
        Worst:   O(n*n)  — reverse-sorted input
    Space Complexity: O(1) auxiliary (in-place)

    Args:
        data: A list of integers to be sorted. The list is modified in-place
              and also returned for API consistency.

    Returns:
        The same list reference, now sorted in ascending order.
    """
    length = len(data)
    for i in range(1, length):
        key = data[i]
        j = i - 1
        # shift elements of the sorted segment forward to find the correct position for key
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]  # shift element forward
            j -= 1
        data[j + 1] = key  # place key in its correct position
    return data


def timsort_builtin(data: list[int]) -> list[int]:
    """Sort a list of integers using Python's built-in Timsort via sorted().

    Timsort is a hybrid merge-sort / insertion-sort algorithm optimised for
    real-world data patterns. It exploits existing ordered subsequences
    ("runs") to achieve near-linear performance on partially sorted inputs.

    Time Complexity:
        Best:    O(n)       — already sorted / few runs
        Average: O(n log n)
        Worst:   O(n log n)
    Space Complexity: O(n) auxiliary

    Args:
        data: A list of integers to be sorted. A new sorted list is returned;
              the original list is not modified.

    Returns:
        A new list containing all elements in ascending order.
    """
    return sorted(data)

# benchmarking
def generate_random_list(size: int) -> list[int]:
    """Generate a list of random integers within predefined bounds.

    Uses a fixed seed (RANDOM_SEED) to guarantee reproducibility across
    runs, ensuring both algorithms receive identical input sequences.

    Args:
        size: The number of random integers to generate.

    Returns:
        A list of *size* random integers in [RANDOM_LOWER_BOUND, RANDOM_UPPER_BOUND].
    """
    random.seed(RANDOM_SEED)
    return [random.randint(RANDOM_LOWER_BOUND, RANDOM_UPPER_BOUND) for _ in range(size)]

def measure_execution_time(func, data: list[int]) -> float:
    """Measure wall-clock execution time of a sorting function.

    Uses time.perf_counter() for the highest available resolution on the
    platform, which is more precise than time.time() for short intervals.

    Args:
        sort_func: A callable that accepts a list[int] and returns a sorted
                   list[int].
        data: The input list to sort. A shallow copy is passed to the
              function so the original remains unmodified.

    Returns:
        Elapsed time in seconds as a float.
    """
    data_copy = data.copy()  # ensure original data 

    start = time.perf_counter()
    func(data_copy)
    end = time.perf_counter()

    return end - start

# report

def print_header() -> None:
    """Print the benchmark header with column titles."""
    print(f"\n{SEPARATOR}")
    print("       benchmark: insertion sort O(n*n) vs timsort O(n log n)") # so para ficar botininho no meio
    print(SEPARATOR)
    print(
        f"  {'n':>10}  |  {'insertion sort':>16}  |  "
        f"{'timsort (sorted)':>16}  |  {'speedup':>10}"
    )
    print(SUB_SEPARATOR)

def print_rows(size: int, time_insertion: float, time_timsort: float) -> None:
    """Print a single benchmark result row.

    Args:
        size: Input list size.
        time_insertion: Insertion Sort elapsed time in seconds.
        time_timsort: Timsort elapsed time in seconds.
    """
    speedup = time_insertion / time_timsort if time_timsort > 0 else float("inf")

    print(
        f"  {size:>10,}  |  {time_insertion:>14.6f} s  |  "
        f"{time_timsort:>14.6f} s  |  {speedup:>8.1f}x"
    )

def print_footer() -> None:
    """Print the benchmark footer with methodology notes."""
    print(SUB_SEPARATOR)
    print("notes:")
    print("timer: time.perf_counter() (highest resolution clock)")
    print("seed:  fixed (RANDOM_SEED = 42) for reproducibility")
    print("each algorithm receives an identical copy of the input")
    print(f"{SEPARATOR}\n")

# main entry point

def main() -> None:
    """Execute the full benchmark suite across all configured input sizes.
    
    For each size in INPUT_SIZES, generates a random list, benchmarks both
    Insertion Sort and Python's built-in sorted(), and prints a formatted
    comparison table including the speedup factor.
    """
    print_header()

    for size in INPUT_SIZES:
        data = generate_random_list(size)

        time_insertion = measure_execution_time(insertion_sort, data)
        time_timsort = measure_execution_time(timsort_builtin, data)

        print_rows(size, time_insertion, time_timsort)

    print_footer()

if __name__ == "__main__":
    main()