def check_sorted(array: list[int]) -> bool:
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            return False
    return True


array = [5, 4, 6, 7, 8]
array2 = [1, 2, 3, 4, 5]
print(check_sorted(array))
print(check_sorted(array2))


def check_sorted_when_rotated(array: list[int]) -> bool:
    cyclic_point = 0
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            cyclic_point += 1
        if cyclic_point > 1:
            return False
    return True if array[len(array) - 1] < array[0] else False


cyclic_array = [5, 6, 7, 1, 2, 3, 4, 6]
print(check_sorted_when_rotated(cyclic_array))
