def largest_elem(arr: list[int]) -> int:
    biggest_index = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[biggest_index]:
            biggest_index = i
    return arr[biggest_index]


def largest_and_smallest_elem(arr: list[int]) -> tuple[int, int]:
    smallest_index, biggest_index = 0, 0

    for i in range(1, len(arr)):
        if arr[i] > arr[biggest_index]:
            biggest_index = i
        if arr[i] < arr[smallest_index]:
            smallest_index = i
    return arr[biggest_index], arr[smallest_index]


array = [1, 2, 0, 100, 30, -30]

print(largest_elem(arr=array))
