class Solution:
    def remove_duplicate(self, nums: list[int]) -> int:
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


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution()
print(solution.remove_duplicate(nums))
