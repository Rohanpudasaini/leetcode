class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_set = {}
        level = len(nums) // 3
        result = set()
        for num in nums:
            if hash_set.get(num):
                hash_set[num] += 1
                if hash_set[num] > level:
                    result.add(num)
            else:
                hash_set[num] = 1
                if level < 1:
                    result.add(num)
        return list(result)        