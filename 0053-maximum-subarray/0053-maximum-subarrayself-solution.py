# # class Solution:
# #     def maxSubArray(self, nums: List[int]) -> int:
# #         length = len(nums)
# #         maximum = -1000000000000
# #         for i in range(length):
# #             sum = 0
# #             for j in range(i, length):
# #                 sum += nums[j]

# #                 maximum = max(maximum, sum)
# #         return maximum
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:            
#         res = nums[0]
#         total = 0

#         for n in nums:
#             if total < 0:
#                 total = 0

#             total += n
#             res = max(res, total)
        
#         return res
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=0
        max_sum=-99999
        for num in nums:
            if num > max_sum:
                max_sum = num
            cur_sum += num
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum 

        