# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# initial thought: Sliding window approach if a word is repeted break
# if a word is not repeated increase the window size and count, store in list
# return max of list

# Working but very bad implementation
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        final_list = []
        
        for i in range(len(s)-1):
            count = 1
            visited_node= [s[i]]
            for j in range(i+1, len(s)):
                if s[j] == s[i] or s[j] in visited_node:
                    break
                else:
                    visited_node.append(s[j])
                    count +=1
            final_list.append(count)
        return max(final_list)
    
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb")) # 3
print(solution.lengthOfLongestSubstring("bbbbb")) # 1
print(solution.lengthOfLongestSubstring("abcdefghasdf")) # 8
print(solution.lengthOfLongestSubstring("a")) # 8



        