class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurance = {}
        for num in nums:
            if occurance.get(num):
                occurance[num] += 1
            else:
                occurance[num] = 1
        max_occurance = 0
        max_value = 0
        for key, value in occurance.items():
            if value > max_occurance:
                max_occurance = value
                max_value = key
        return max_value
            
        
        