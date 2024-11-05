# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        change = 0
        for i in range(len(s)//2):
            if s[i*2] != s[i*2+1]:
                change +=1
        return change
    
solution = Solution()
print(solution.minChanges("11000111")) # 1

        