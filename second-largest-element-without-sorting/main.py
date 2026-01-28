from typing import Union


def second_largest(array: list[int]) -> int:
    largest = -2
    second_largest = -1
    for i in range(len(array)):
        if array[i] > largest:
            second_largest, largest = largest, array[i]
        elif array[i] > second_largest:
            second_largest = array[i]
    return second_largest


arry = [1, 1, 2, 4, 7, 7, 5]

print(second_largest(arry))


def second_largest_without_duplicate(array: list[int]) -> Union[int, float]:
    largest, second_largest = float("-inf"), float("-inf")
    for i in range(len(array)):
        if array[i] > largest:
            second_largest, largest = largest, array[i]
        elif array[i] > second_largest and arry[i] != largest:
            second_largest = array[i]
    return second_largest


def second_largest_and_smallest_without_duplicate(
    array: list[int],
) -> tuple[Union[int, float], Union[int, float]]:
    largest, second_largest = float("-inf"), float("-inf")
    smallest, second_smallest = float("inf"), float("inf")
    for i in range(len(array)):
        if array[i] > largest:
            second_largest, largest = largest, array[i]
        elif array[i] > second_largest and arry[i] != largest:
            second_largest = array[i]
        if array[i] < smallest:
            second_smallest, smallest = smallest, array[i]
        elif array[i] < second_smallest and array[i] != smallest:
            second_smallest = array[i]
    return second_largest, second_smallest


# smallest, second_smallest = 10001, 10000

print(second_largest_without_duplicate(arry))
print(second_largest_and_smallest_without_duplicate(arry))
