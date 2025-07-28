class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(set(nums)) == 1 and nums[0] == 0:
            return [[0,0,0]]
        answer = set()
        for i in range(len(nums)):
            hash_set = set()
            for j in range(i+1, len(nums)):
                remaining = -(nums[i] + nums[j])
                if remaining in hash_set:
                    result = tuple(sorted([nums[i], nums[j], remaining]))
                    answer.add(result)
                else:
                    hash_set.add(nums[j])
        return list(answer)
        
        