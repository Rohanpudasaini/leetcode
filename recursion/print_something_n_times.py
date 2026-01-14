# Print name n times using recursion
def print_n_times(n: int):
    if n == 0:
        return n
    print_n_times(n - 1)
    print("Rohan")
    return 0


# Print 1 to N using recursion
def print_to_n(num: int, current: int) -> None:
    if num == current:
        return
    print(current + 1)
    print_to_n(num, current + 1)


# Print from N to 1 using recursion
def print_n_to_1(num: int):
    if num == 0:
        return
    print(num)
    print_n_to_1(num - 1)


# Sum of first N number
def sum_up_to_n(n: int, current: int = 0, sum: int = 0) -> int:
    if current - 1 == n:
        return sum
    return sum_up_to_n(n, current + 1, current + sum)


# Factorial of N using recursion
# Factorial of 3 = 3x2x1
# Base case factorial of 0 is 1
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print_n_times(5)
print_to_n(5, 0)
print_n_to_1(5)
print(sum_up_to_n(4))
print(factorial(10))
