# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9)) # [0, 1]
print(solution.twoSum([3,2,4], 6)) # [1, 2]
            
            
            

       