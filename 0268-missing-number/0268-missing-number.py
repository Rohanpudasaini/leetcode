class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        input = [x for x in range(len(nums)+1)]
        return set(input).difference(nums).pop()
        