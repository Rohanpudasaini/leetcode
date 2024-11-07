# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
############################################################################################################
############################################################################################################

# Not Solved by me will be back again in future
# TODO: Future me Come back to solve this problem  after learning more about bitwise operations
############################################################################################################
############################################################################################################



# class Solution(object):
#     def largestCombination(self, candidates):
#         """
#         :type candidates: List[int]
#         :rtype: int
#         """
#         another_hash_map = {}
#         if len(candidates) == 1:
#             return candidates[0]
#         for i in range(len(candidates)-1):
#             hash_map = {}
#             for j in range(i+1, len(candidates)):
#                 if candidates[i] & candidates[j] == 0:
#                     continue
#                 else:
#                     bit_and = candidates[i] & candidates[j]
#                     if hash_map.get(bit_and):
#                         hash_map[bit_and] +=1
#                     else:
#                         hash_map[bit_and] = 1
#             another_hash_map[i]=max(hash_map.values()) + 1
#             print(hash_map)
#         print(another_hash_map)
#         return max(another_hash_map.values())
            
        
            
        
# solution = Solution()
# print(solution.largestCombination([10,72,58,33,36,70,12,88,9,48,78,97,87,19,78,9,47,73])) # 16

class Solution:
    def largestCombination(self, candidates):
        # Initialize a list to store the count of each bit position.
        bit_count = [0] * 24
        for i in range(24):
            for num in candidates:
                # Check if the i-th bit is set.
                if (num & (1 << i)) != 0:
                    bit_count[i] += 1

        return max(bit_count)