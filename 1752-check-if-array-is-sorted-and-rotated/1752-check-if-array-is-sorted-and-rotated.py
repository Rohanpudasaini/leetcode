class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_arry = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            else:
                if nums[i+1:] + nums[:i+1] == sorted_arry:
                    return True
                return False
        return True
        