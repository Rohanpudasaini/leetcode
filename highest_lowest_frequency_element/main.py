# Example
'''
Docstring for highest_lowest_frequency_element.main
Example 1:
Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.


Example 2:
Input: array[] = {2,2,3,4,4,2};
Output: 2 3
Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.
            
''' 
# My solution
# array = [10,5,10,15,10,5,15,5,15,5]
array = [2,2,3,4,4,2]

class Solution:
    def higher_lower_frequency_elements(self, nums: list[int]) -> tuple[int]:
        # higher
        # Lower
        # HashSet to store frequenct of each number
        highest_frequency = 0
        lowest_frequency = 1000
        lowest_element = -1
        highest_element = -1
        hash_set = {}
        for num in nums:
            hash_set[num] = hash_set.get(num, 0) + 1
            if hash_set[num] >= hash_set.get(highest_element, 0):
                highest_frequency = hash_set[num]
                highest_element = num
            if hash_set[num] <= hash_set.get(lowest_element, 1000):
                lowest_frequency = hash_set[num]
                lowest_element = num
        print(hash_set)
        print(highest_frequency, lowest_frequency)
        return(highest_element, lowest_element)

sol = Solution()
sol.higher_lower_frequency_elements(array)
                
# Solution according to chat

class ChatSolution:
    def higher_lower_frequency_elements(self,nums: list[int]) -> tuple[int]:
        hash_set = {}
        lowest_frequency = float("inf")
        highest_frequency = float("-inf")
        for num in nums:
            hash_set[num] = hash_set.get(num,0) + 1
        for key, value in hash_set.items():
            if value > highest_frequency:
                highest = key
                highest_frequency = value
            if value < lowest_frequency:
                lowest = key
                lowest_frequency = value
        print(hash_set)
        return (highest, lowest)

sol1 = ChatSolution()
print(sol1.higher_lower_frequency_elements(array))