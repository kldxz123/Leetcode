class Solution(object):
	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		a = [1]*n
		count = 0

		i = 2
		while i < n:
			if a[i] == 1:
				count += 1
				j = 2
				while i*j<n:
					a[i*j] = 0
					j += 1
			i = i + 1

		return count
sol = Solution()
print(sol.countPrimes(14))

        