class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        x1 = int(str(x)[::-1])

        if x1 == x:
            return True
        else:
            return False
