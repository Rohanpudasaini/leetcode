class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # occurance = {}
        # for num in nums:
        #     if occurance.get(num):
        #         occurance[num] +=1
        #     else:
        #         occurance[num] = 1
        # if not occurance.get(1):
        #     occurance[1] = 0
        # if not occurance.get(2):
        #     occurance[2] = 0
        # if not occurance.get(0):
        #     occurance[0] = 0
        # nums[0:occurance[0]] =[0]* occurance[0]
        # nums[occurance[0]: occurance[0]+occurance[1]] = [1]*occurance[1]
        # nums[occurance[0]+occurance[1]: occurance[0]+occurance[1]+occurance[2]] = [2]*occurance[2]
        low = mid = 0
        high = len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid +=1
                low +=1
            elif nums[mid] == 1:
                mid +=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -=1





        