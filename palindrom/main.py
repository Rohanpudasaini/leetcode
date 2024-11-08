class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string_form = str(x)
        length = len(string_form)-1
        for i in range(len(string_form)):
            if string_form[i] == string_form[length-i]:
                continue
            return False
        return True
        


        