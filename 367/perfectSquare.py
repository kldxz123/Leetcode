class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        i = 0
        c = 0
        while i < num:
            c += 1
            i = c*c
        if i == num:
            return True
        else:
            return False