class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        sum = 0
        while sum < n:
        	sum += i
        	i += 1
        if sum == n:
        	return i - 1
        else:
        	return i - 2