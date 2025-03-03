class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hash_set = {}
        for single_list in nums1+ nums2:
            key, value = single_list[0], single_list[1]
            hash_set[key] = value if not hash_set.get(key) else hash_set[key] + value
        return [[x, hash_set[x]] for x in sorted(list(hash_set.keys()))]
        