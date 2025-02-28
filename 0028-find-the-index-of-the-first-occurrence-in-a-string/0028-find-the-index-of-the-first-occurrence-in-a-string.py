class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window_size = len(needle)
        if len(haystack) < window_size:
            return -1
        if haystack == needle:
            return 0
        for current_index in range(len(haystack)-window_size+1):
            if haystack[current_index:current_index+window_size] == needle:
                return current_index
        return -1

        