# F(n) = 2F(n-1) + n*n
# base case F(1) = 2

"""
Task:

1. Implement this funtion in Python using recursion.

2. The program must read an value n from the user and print F(n).

Tips:

1. The functions musr call himself until solve the base case

2. The complexity of this function is O(2^n), so be careful with big values of n.

3. You can use the math library to calculate the close formula.
"""

def F(n):
    if n == 1:
        return 2
    return 2 * F(n - 1) + n * n


n = int(input("Enter a value for n: "))
print(f"F({n}) = {F(n)}")