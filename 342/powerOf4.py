class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num > 1:
        	p = num & 3 
        	if p != 0:
        		return False
        	num = num >> 2
        if num == 1:
        	return True
        else:
        	return False

sol = Solution()
print(sol.isPowerOfFour(7))