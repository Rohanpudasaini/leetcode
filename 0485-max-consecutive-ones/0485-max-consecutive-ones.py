class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        previous_best = 0
        current_best = 0
        for num in nums:
            if num == 1:
                current_best += 1
            else:
                previous_best = current_best
                current_best = 0
        return max(previous_best, current_best)
        