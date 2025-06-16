class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        for i in range(1, len(nums)):
            if nums[-i] > nums[-i-1]:
                index = len(nums) - i-1
                break
        if index == -1:
            nums[:] = nums[::-1]
            return
        for j in range(-1, index+1-len(nums)-1, -1):
            if nums[j] > nums[index]:
                nums[index], nums[j] = nums[j], nums[index]
                break
        nums[index+1:] = nums[index+1:][::-1]
        
        

        