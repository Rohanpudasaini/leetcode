class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        total_length = len(nums)
        max_sum_of_partation = []
        partation = []
        for i in range(total_length-1):
            if nums[i] < nums[i+1]:
                continue
            else:
                partation.append(i)
        if not partation:
            partation.append(total_length-1)
        for i in range(len(partation)):
            if not max_sum_of_partation:
                max_sum_of_partation.append(sum(nums[:partation[i]+1]))
            else:
                max_sum_of_partation.append(sum(nums[partation[i-1]+1:partation[i]+1]))
        if partation[-1] != total_length-1:
            max_sum_of_partation.append(sum(nums[partation[-1]+1:]))
        return max(max_sum_of_partation)

        