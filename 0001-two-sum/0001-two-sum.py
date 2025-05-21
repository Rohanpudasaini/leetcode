class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        # Consicutive two element
        # for i in range(length):
        #     if nums[i] == target:
        #         return [i]
        #     sum = nums[i]
        #     for j in range(i+1, length):
        #         sum += nums[j]
        #         if sum > target:
        #             break
        #         if sum == target:
        #             return [x for x in range(i,j+1)]
        hash_map = {nums[i]: i for i in range(length)}
        for i in range(length):
            difference = target - nums[i]
            valid = hash_map.get(difference)
            if valid and i != valid:
                return [valid, i] if valid < i else [i, valid]

                