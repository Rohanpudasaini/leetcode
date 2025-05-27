class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        occurance = {}
        for num in nums:
            if occurance.get(num):
                occurance[num] +=1
            else:
                occurance[num] = 1
        if not occurance.get(1):
            occurance[1] = 0
        if not occurance.get(2):
            occurance[2] = 0
        if not occurance.get(0):
            occurance[0] = 0
        nums[0:occurance[0]] =[0]* occurance[0]
        nums[occurance[0]: occurance[0]+occurance[1]] = [1]*occurance[1]
        nums[occurance[0]+occurance[1]: occurance[0]+occurance[1]+occurance[2]] = [2]*occurance[2]

        