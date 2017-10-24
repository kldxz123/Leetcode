class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
        	return 0
        if n == 0:
        	return 1
        if n > 0:
        	result = pow(x,n)
        else:
        	n = abs(n)
        	x = 1/x
        	result = pow(x,n)



        return result