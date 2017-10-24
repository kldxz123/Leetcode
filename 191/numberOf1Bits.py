class Solution(object):
	def hammingWeight(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		b = bin(n)
		c = 0
		for i in b:
			if i == '1':
				c += 1

		return c