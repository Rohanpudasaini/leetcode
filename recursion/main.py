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
    if current > n:
        return sum
    return sum_up_to_n(n, current + 1, current + sum)


# Factorial of N using recursion
# Factorial of 3 = 3x2x1
# Base case factorial of 0 is 1
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def print_array_in_reverse(array: list, current: int = 0) -> None:
    if current == len(array):
        return
    print_array_in_reverse(array, current + 1)
    print(array[current])


def reverse_array(array: list, current: int = 0, new_array=[]) -> list:
    if current >= len(array):
        return []
    new_array = reverse_array(array, current + 1, new_array)
    new_array.append(array[current])
    return new_array


# check if a string is palindrom or not using recursion
# Brute force
def check_palindrom(s: str) -> bool:
    string_array = list(s)
    if s == "".join(reverse_array(string_array)):
        return True
    return False


# Optimal using recursion


def is_palindrom(i: int, s: str) -> bool:
    if i >= len(s) // 2:
        return True
    if s[i] != s[len(s) - i - 1]:
        return False
    return is_palindrom(i + 1, s)


# Write fibonachi number upto N
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    num1, num2 = fib(n - 1), fib(n - 2)
    # print(f"{num1} + {num2}")
    return num1 + num2


array = [1, 2, 3, 4, 5]
print_n_times(5)
print_to_n(5, 0)
print_n_to_1(5)
print(sum_up_to_n(4))
print(factorial(10))

print_array_in_reverse(array)
print(reverse_array(array))

print(check_palindrom("ABA"))
print(is_palindrom(0, "MADAM"))
# print(fib(1))
# print(fib(2))
# print(fib(3))
# print(fib(4))
# print(fib(5))
print(fib(600))
