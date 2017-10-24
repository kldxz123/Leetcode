import sys

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        c = 0
        if dividend > 0 and divisor < 0:
        	c = 1
        	divisor = 0 - divisor

        if dividend < 0 and divisor > 0:
        	dividend = 0 - dividend
        	c = 1
        if dividend < 0 and divisor < 0:
        	divisor = 0 - divisor
        	dividend = 0 - dividend

        max_int = 2147483647
        result = 0
        if divisor == 1:
        	result = min(max_int,dividend)
        	if c == 0:
        		return result
        	else:
        		return 0 - result


        while result < max_int and dividend >= divisor:
        	dividend -= divisor
        	result += 1
        if c == 0:
        	return result
        else:
        	return 0 - result

sol = Solution()
print(sol.divide(-2147483647,-1))

        