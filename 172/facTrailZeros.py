class Solution(object):
	def trailingZeroes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		count2 = 0
		count5 = 0
		c = 1
		while n:
			n = int(n / 5)
			count5 += n
		return count5
sol = Solution()
print(sol.trailingZeroes(10))
