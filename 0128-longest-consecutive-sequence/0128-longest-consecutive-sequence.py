class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        longest = 1
        for num in nums:
            if num-1 not in nums:
                count = 1
                x = num
                while x+1 in nums:
                    x += 1
                    count += 1
            longest = max(longest, count)
        return longest

        
            

        