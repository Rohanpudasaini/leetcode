class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        left = 0
        right = 1
        length = len(nums)
        while right <=length-1:
            if nums[left] > 0 and nums[right]>0:
                right += 1
            elif nums[left] < 0 and nums[right] < 0:
                right += 1
            elif (nums[left] > 0 and nums[right] < 0) or (nums[left] < 0 and nums[right] > 0):
                if nums[left] < 0: 
                    nums[left], nums[right] = nums[right], nums[left]
                nums[left+1], nums[right] = nums[right], nums[left+1]

                left +=2
                right +=1
        return nums

            
        