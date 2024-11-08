# class Solution(object):
#     def isPalindrome(self, x):
#         if x < 0 or (x % 10 == 0 and x != 0 ):
#             return False
        
#         reverse = 0
#         while x > reverse:
#             reverse = reverse * 10 + x % 10
#             x //= 10

#         return x == reverse or x == reverse // 10


# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         string_form = str(x)
#         length = len(string_form)-1
#         for i in range(len(string_form)):
#             if string_form[i] == string_form[length-i]:
#                 continue
#             return False
#         return True
        