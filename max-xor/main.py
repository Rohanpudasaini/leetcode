# https://leetcode.com/problems/maximum-xor-for-each-query/

# TODO: Understand the problem and implement the solution
# TODO: self, Solution copied, comeback and re try once learned more about bit manipulation
class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        prefix_xor = [0] * len(nums)
        prefix_xor[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_xor[i] = prefix_xor[i - 1] ^ nums[i]
        ans = [0] * len(nums)

        mask = (1 << maximumBit) - 1
        for i in range(len(nums)):
            # find k to maximize value
            current_xor = prefix_xor[len(prefix_xor) - 1 - i]
            ans[i] = current_xor ^ mask

        return ans