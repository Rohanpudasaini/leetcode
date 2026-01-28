class Solution:
    def check(self, nums: List[int]) -> bool:
        cyclic_point = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                cyclic_point += 1
            if cyclic_point > 1:
                return False
        if (cyclic_point != 0 and nums[len(nums)-1] <= nums[0]) or cyclic_point==0:
            return True
        return False
        