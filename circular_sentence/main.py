# class Solution(object):
#     current_character = ''
#     is_circular = False
#     def isCircularSentence(self, sentence:str):
#         """
#         :type sentence: str
#         :rtype: bool
#         """
#         words_in_sentence = sentence.strip().split(' ')
#         self.is_circular = words_in_sentence[0][0] == words_in_sentence[-1][-1]
#         for iteration, word in enumerate(words_in_sentence):
#             if not self.is_circular:
#                 break
#             if iteration == 0:
#                 self.current_character = word[-1]
#                 continue
#             if word[0] == self.current_character:
#                 self.is_circular = True
#             else:
#                 self.is_circular = False
#             self.current_character = word[-1]
            
#         return self.is_circular

class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        
        for i in range(len(sentence)):
            if sentence[i] == " ":
                if sentence[i - 1] != sentence[i + 1]:
                    return False
        return sentence[0] == sentence[-1]

    

solution = Solution()
print(solution.isCircularSentence('Leetcode eisc cool')) # False

    
        
        