class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 3:
            return True
        k = n % 4
        if k == 0:
            return False
        else:
            return True