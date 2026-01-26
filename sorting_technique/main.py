# Write code for selection sort
# Select a minimum and swap with the first place
# Time complexity is o(n**2)
# Space complexity is O(1)
def selection_sort(array: list) -> list:
    for i in range(len(array)):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]
    return array


# Bubble sort
# Compate two elements and move swap if they are in wrong place
def bubble_sort(array: list) -> list:
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 2):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# Time complexity O(N**2)
# Space Complexity O(1)
def insertion_sort(array: list) -> list:
    for i in range(len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


def merge(array, left, mid, right):
    print(array[left:mid])
    print(array[mid:right])
    while left <= mid and mid <= right:
        if array[left] > array[mid]:
            array[left], array[mid] = array[mid], array[left]
            left += 1
        elif array[left] == array[mid]:
            left += 1
            mid += 1
        else:
            mid += 1
    return


def merge_sort(array: list, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)


array = [9, 5, 2, 3]
merge_sort(array, 0, len(array))
# print(insertion_sort(array))
# print(selection_sort(array))

# print(bubble_sort(array))
