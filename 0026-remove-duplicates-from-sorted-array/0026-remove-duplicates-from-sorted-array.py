class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        left, right = 0, 1
        while right < length:
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
        print(nums)
        return left + 1
        