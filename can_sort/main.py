# https://leetcode.com/problems/find-if-array-can-be-sorted/

class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        for i in range(n-1):
            if nums[i] <= nums[i+1]:
                continue
            else:
                if bin(nums[i]).count('1') == bin(nums[i+1]).count('1'):
                    temp = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp
                else:
                    return False
        for i in range(n-1, 0, -1):
            if nums[i] >= nums[i-1]:
                continue
            else:
                if bin(nums[i]).count('1') == bin(nums[i-1]).count('1'):
                    temp = nums[i]
                    nums[i] = nums[i - 1]
                    nums[i - 1] = temp
                else:
                    return False
        return True
        


    

solution = Solution()
print(solution.canSortArray([3,16,8,4,2])) # false
print(solution.canSortArray([8,4,2,30,15])) # True
print(solution.canSortArray([1,2,3,4,5])) # True
print(solution.canSortArray([20,16])) # False

