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


array = [9, 5, 2, 3, 6, 1, 10]
print(selection_sort(array))

print(bubble_sort(array))
