# # #  https://leetcode.com/problems/minimum-array-end/


# # class Solution(object):
# #     def minEnd(self, n, x):
# #         """
# #         :type n: int
# #         :type x: int
# #         :rtype: int
# #         """
# #         final_bit = x
# #         bit_and = x
# #         new_list = [x]
# #         for i in range(1, n):
# #             if (x + i) & final_bit == bit_and:
# #                 new_list.append(x + i)
# #                 final_bit = x + i
# #         return final_bit

# #Learned from editorial
# class Solution(object):
#     def minEnd(self, n, x):
#         result = x
#         while n > 1:
#             result = (result + 1) | x
#             n -= 1
#         return result

# # Test cases
# solution = Solution()
# print(solution.minEnd(3, 4))  # 6
# print(solution.minEnd(2, 7))  # 15


## Here is the one accepted by the leetcode.

class Solution:
    def minEnd(self, n, x):

        result = 0
        # Reducing n by 1 to exclude x from the iteration
        n -= 1

        # Step 1: Initialize lists to hold the binary representation of x and n-1
        binaryX = [0] * 64  # Binary representation of x
        binaryN = [0] * 64  # Binary representation of n-1

        # Step 2: Build binary representations of x and n-1
        for i in range(64):
            bit = (x >> i) & 1  # Extract i-th bit of x
            binaryX[i] = bit

            bit = (n >> i) & 1  # Extract i-th bit of n-1
            binaryN[i] = bit

        posX = 0
        posN = 0

        # Step 3: Combine binary representation of x and n-1
        while posX < 63:
            # Traverse binaryX until we find a 0 bit
            while binaryX[posX] != 0 and posX < 63:
                posX += 1
            # Copy bits from binaryN (n-1) into binaryX (x) starting from the first 0
            binaryX[posX] = binaryN[posN]
            posX += 1
            posN += 1

        # Step 4: Rebuild the final result from the combined binary representation
        for i in range(64):
            if binaryX[i] == 1:
                # convert binary bit to decimal value
                result += pow(2, i)

        return result
