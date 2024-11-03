# Link: https://leetcode.com/problems/rotate-string/
# Simple looping?
# For length of string, loop through and shift the 1 and -1 position and check if the string is equal to the goal
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
