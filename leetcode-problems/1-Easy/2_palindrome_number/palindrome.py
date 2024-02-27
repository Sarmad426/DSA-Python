"""
Leetcode Palindrome number (Easy)
"""


class CheckPalindrome(object):
    """Palindrome number solution"""

    def is_palindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        temp = str(x)
        string = ""
        while x > 0:
            digit = x % 10
            x = int(x / 10)
            string += str(digit)
        return temp == string
