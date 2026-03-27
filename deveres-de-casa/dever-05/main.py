"""
Complexity for

1. merge sort

2. matrix multiplication

3. recurrence:

a. T(n) = 2T(n/4) + sqrt(n)
b. T(n) = 2T(n/4) + n
c. T(n) = 16T(n/4) + n*n

"""

# ============================================================
# RESPOSTAS / ANSWERS
# ============================================================

# Master Theorem: T(n) = aT(n/b) + f(n)
# Compare f(n) with n^(log_b(a))

# ------------------------------------------------------------
# 1. Merge Sort
# ------------------------------------------------------------
# T(n) = 2T(n/2) + n
# a = 2, b = 2
# log_b(a) = log_2(2) = 1
# f(n) = n = n^1
# f(n) = Theta(n^(log_b(a))) -> Case 2
#
# Complexity: O(n * log(n))

# ------------------------------------------------------------
# 2. Matrix Multiplication (naive)
# ------------------------------------------------------------
# Standard algorithm: 3 nested loops
#
# Complexity: O(n^3)

# ------------------------------------------------------------
# 3a. T(n) = 2T(n/4) + sqrt(n)
# ------------------------------------------------------------
# a = 2, b = 4
# log_b(a) = log_4(2) = 0.5
# f(n) = sqrt(n) = n^0.5
# f(n) = Theta(n^(log_b(a))) -> Case 2
#
# Complexity: O(sqrt(n) * log(n))

# ------------------------------------------------------------
# 3b. T(n) = 2T(n/4) + n
# ------------------------------------------------------------
# a = 2, b = 4
# log_b(a) = log_4(2) = 0.5
# f(n) = n = n^1
# n^1 > n^0.5 -> Case 3
# Check regularity: 2 * (n/4) <= c * n for c < 1? Yes, n/2 <= cn
#
# Complexity: O(n)

# ------------------------------------------------------------
# 3c. T(n) = 16T(n/4) + n^2
# ------------------------------------------------------------
# a = 16, b = 4
# log_b(a) = log_4(16) = 2
# f(n) = n^2
# f(n) = Theta(n^(log_b(a))) -> Case 2
#
# Complexity: O(n^2 * log(n))


# ============================================================
# IMPLEMENTATIONS
# ============================================================

import math

# ------------------------------------------------------------
# 1. Merge Sort - O(n log n)
# ------------------------------------------------------------

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ------------------------------------------------------------
# 2. Matrix Multiplication - O(n^3)
# ------------------------------------------------------------

def matrix_multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


# ------------------------------------------------------------
# 3a. T(n) = 2T(n/4) + sqrt(n) - O(sqrt(n) * log(n))
# ------------------------------------------------------------

def T_a(n):
    if n <= 1:
        return 1
    return 2 * T_a(n // 4) + int(math.sqrt(n))


# ------------------------------------------------------------
# 3b. T(n) = 2T(n/4) + n - O(n)
# ------------------------------------------------------------

def T_b(n):
    if n <= 1:
        return 1
    return 2 * T_b(n // 4) + n


# ------------------------------------------------------------
# 3c. T(n) = 16T(n/4) + n^2 - O(n^2 * log(n))
# ------------------------------------------------------------

def T_c(n):
    if n <= 1:
        return 1
    return 16 * T_c(n // 4) + n * n


# ============================================================
# TESTS
# ============================================================

if __name__ == "__main__":
    # Test Merge Sort
    print("=" * 50)
    print("1. Merge Sort")
    print("=" * 50)
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr}")
    print(f"Sorted:   {merge_sort(arr)}")

    # Test Matrix Multiplication
    print("\n" + "=" * 50)
    print("2. Matrix Multiplication")
    print("=" * 50)
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"A x B = {matrix_multiply(A, B)}")

    # Test Recurrences
    print("\n" + "=" * 50)
    print("3. Recurrences")
    print("=" * 50)

    n = 64
    print(f"\nFor n = {n}:")
    print(f"  T_a(n) = 2T(n/4) + sqrt(n) = {T_a(n)}")
    print(f"  T_b(n) = 2T(n/4) + n       = {T_b(n)}")
    print(f"  T_c(n) = 16T(n/4) + n^2    = {T_c(n)}")
