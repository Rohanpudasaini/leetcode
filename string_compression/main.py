# https://leetcode.com/problems/string-compression-iii/

# Initial thought
# 1. iterate over the word
# 2. for each word maintain key value pair with key as word and value as count
# 3. if the word is already present then increment the count
# 4. if the word is not present then add the word to the dictionary with count as 1
# 5. iterate over the dictionary and create a compressed string

class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        # comp = {}
        # for each_word in word:
        #     if each_word in comp:
        #         comp[each_word] += 1
        #     else:
        #         comp[each_word] = 1
        # compressed = []
        # for key, value in comp.items():
        #     if value > 9:
        #         compressed.extend(["9",key, str(value-9),key])
        #     else:
        #         compressed.extend([str(value),key])
        #     print(compressed)
        
        # return ''.join(compressed)
     ####   
        # This might have worked but the problem is with how python interpret its dictionary.
        #  While iterating over the dictionary, the order of the keys is not maintained. 
        # So the compressed string will not be in the order of the word. 
        # So we need to come up with a different approach.
    ####
        ############################################################################################################

        # current_char = word[0]
        # count = 1
        # comp = []
        # for i in range(len(word)):
        #     if word[i] != current_char:
        #         comp.extend([str(count), current_char])
        #         count = 1
        #         current_char = word[i]
        #     elif word[i] == current_char and count > 9:
        #         comp.extend(['9', current_char])
        #         count = 0
        #     else:
        #         count += 1
        #     if i == len(word)-1:
        #         if count >9:
        #             comp.extend(['9', current_char, str(count-9), current_char])
        #         else:
        #             comp.extend([str(count), current_char])
        # return ''.join(comp)

        ############################################################################################################

        # compressed = []
        # count = 1
        
        # for i in range(1, len(word) + 1):
        #     # Check if we're at the last character or if the next character is different
        #     if i < len(word) and word[i] == word[i - 1]:
        #         count += 1
        #     else:
        #         # Handle cases where count > 9
        #         while count > 9:
        #             compressed.extend(["9", word[i - 1]])
        #             count -= 9
        #         if count > 0:
        #             compressed.extend([str(count), word[i - 1]])
                
        #         count = 1  # Reset count for the next new character
        
        # return ''.join(compressed)

        ############################################################################################################


        comp = []
        count = 0

        curr_char = word[0]

        for c in word:
            if c == curr_char and count < 9:
                count += 1
            else:
                comp.extend([str(count), curr_char])

                curr_char = c
                count = 1

        comp.append(str(count))
        comp.append(curr_char)

        return "".join(comp)
    
solution = Solution()
print(solution.compressedString("aaabcccd")) # 3a1b3c1d       
print(solution.compressedString("abcde"))
print(solution.compressedString("aaaaaaaaaaaaaabb"))
print(solution.compressedString("mrm"))
print(solution.compressedString("fffffffffddddddddddddddddddddddddddddmmmmooooooooooss"))
