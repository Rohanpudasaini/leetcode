class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_index = 0
        negative_index = 1
        length = len(nums)
        new_arry = [0] * length
        for i in range(length):
            if nums[i] > 0:
                new_arry[positive_index] = nums[i]
                positive_index +=2
            else:
                new_arry[negative_index] = nums[i]
                negative_index += 2
        return new_arry


        
        return nums

            
        