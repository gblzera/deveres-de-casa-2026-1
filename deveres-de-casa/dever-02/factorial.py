"""Recursive Factorial Algorithm with Complexity Analysis.

This module implements a factorial calculation using recursion
and measures execution time for different input values.
"""

import sys
import time

# Constants
RECURSION_LIMIT = 2000
TEST_VALUES = [10, 100, 500, 1000]

sys.setrecursionlimit(RECURSION_LIMIT)


def factorial(n):
    """Calculate the factorial of n using recursion.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n (n!).

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def measure_execution_time(func, n):
    """Measure the execution time of a function.

    Args:
        func: The function to be executed.
        n: The argument to pass to the function.

    Returns:
        A tuple containing (result, execution_time).
    """
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


def print_results(timing_results):
    """Print the timing results in a formatted table.

    Args:
        timing_results: A list of tuples (n, execution_time).
    """
    print("-" * 50)
    print("TIME SUMMARY")

    for i, (n, t) in enumerate(timing_results):
        if i == 0:
            print(f"n = {n:<5} | time = {t:.6f}s")
        else:
            previous_time = timing_results[i - 1][1]
            if previous_time > 0:
                ratio = t / previous_time
                print(f"n = {n:<5} | time = {t:.6f}s | {ratio:.2f}x slower")
            else:
                print(f"n = {n:<5} | time = {t:.6f}s")


def print_complexity_analysis():
    """Print the Big O complexity analysis."""
    print()
    print("-" * 50)
    print("COMPLEXITY ANALYSIS (Big O)")
    print("""
TIME COMPLEXITY: O(n)

Why?
- The function calls itself n times until reaching the base case
- Example: factorial(5) -> factorial(4) -> factorial(3) -> factorial(2) -> factorial(1)
- Each call performs only one multiplication (constant operation)
- Therefore: n calls * O(1) each = O(n)

Looking at the measured times, when n increases, the time also increases
proportionally. This confirms that the complexity is linear.

SPACE COMPLEXITY: O(n)

Why?
- Each recursive call uses space on the execution stack
- Since we have n calls stacked before starting to return
- The total space used is proportional to n

CONCLUSION:
Execution time grows LINEARLY with the input size n.
If you double the value of n, the time approximately doubles as well.
""")


def main():
    """Execute the factorial timing measurements."""
    timing_results = []

    print("Calculating factorial...")
    print()

    for n in TEST_VALUES:
        result, execution_time = measure_execution_time(factorial, n)
        timing_results.append((n, execution_time))

        print(f"n = {n}")
        print(f"  Execution time: {execution_time:.6f} seconds")
        print(f"  Result: {result}")
        print()

    print_results(timing_results)
    print_complexity_analysis()


if __name__ == "__main__":
    main()
