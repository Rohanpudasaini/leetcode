def second_largest(array: list[int]) -> int:
    largest = -2
    second_largest = -1
    for i in range(len(array)):
        if array[i] > largest:
            second_largest, largest = largest, array[i]
        elif array[i] > second_largest:
            second_largest = array[i]
    return second_largest


arry = [1, 2, 4, 7, 7, 5]

print(second_largest(arry))


def second_largest_without_duplicate(array: list[int]) -> int:
    largest, second_largest = -2, -1
    for i in range(len(array)):
        if array[i] > largest:
            second_largest, largest = largest, array[i]
        elif array[i] > second_largest and arry[i] != largest:
            second_largest = array[i]
    return second_largest


# smallest, second_smallest = 10001, 10000

print(second_largest_without_duplicate(arry))
