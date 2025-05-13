"""
Brute froce Approch
Using Two loop
O(n^2)"""
# def longest_subarray_with_sum_k(arr, sum) -> list[int]:
#     length = len(arr)
#     longest_length = 0
#     for i in range(length):
#         current_sum = arr[i]
#         for j in range(i+1, length):
#             current_sum += arr[j]
#             if current_sum == sum:
#                 longest_length = max(longest_length, j - i +1)
#     return longest_length

"""
Hash map approch
Use only one loop
O(n)
"""

def longest_subarray_with_sum_k(arr, k) -> list[int]:
    hash_map = {}
    sum = 0
    max_len = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum == k:
            max_len = max(max_len, i+1)
        remaning = sum - k

        if remaning in hash_map:
            length = i - hash_map[remaning]
            max_len = max(max_len, length)
        if sum not in hash_map:
            hash_map[sum] = i
    # print(hash_map)
    return max_len




print(longest_subarray_with_sum_k([1, 2, 2, 4, 5, 1,1,1,0,0,0,0], 3))
print(longest_subarray_with_sum_k([1, 2, 3, 4, 5], 9))