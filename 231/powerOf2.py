class Solution(object):
	def isPowerOfTwo(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		i = 1
		while i < n:
			i = i * 2
		if i == n:
			return True
		else:
			return False