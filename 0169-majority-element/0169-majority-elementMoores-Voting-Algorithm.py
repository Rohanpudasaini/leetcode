class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # occurance = {}
        # for num in nums:
        #     if occurance.get(num):
        #         occurance[num] += 1
        #     else:
        #         occurance[num] = 1
        # max_occurance = 0
        # max_value = 0
        # for key, value in occurance.items():
        #     if value > max_occurance:
        #         max_occurance = value
        #         max_value = key
        # return max_value
        # occurance = {}
        # max_value = max_occurance = 0
        # for num in nums:
        #     occurance[num] = 1 + occurance.get(num, 0)
        #     if occurance[num] > max_occurance:
        #         max_value = num
        #         max_occurance = occurance[num]
        # return max_value
        count = majority = 0
        for num in nums:
            if count == 0:
                majority = num
            
            if num == majority:
                count +=1
            else:
                count -=1
        return majority

        

            
        
        