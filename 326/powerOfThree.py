class Solution(object):
    def isPowerOfThree(self, n):
		if n == 0:
			return True
		a = 3
		while a < n:
			a = a * 3
		if a == n:
			return True
		else:
			return False
        