class Solution:
    def move_zero_to_end(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        left, right = 0, 1
        while right < len(nums):
            if nums[left] != 0:
                left += 1
                right += 1
            elif nums[left] == 0 and nums[right] > 0:
                nums[left], nums[right] = nums[right], nums[left]
            else:
                right += 1
            print(nums)
        return nums


test_nums = [1, 0, 2, 3, 0, 4, 0, 0, 0, 5]
sol = Solution()
print(sol.move_zero_to_end(nums=test_nums))
