class Solution(object):
	def compose(self,n,r):
		if n == 0 or r == 0:
			return 1
		a = 1
		b = 1
		c = 1
		for i in range(n):
			a *= i + 1
		for i in range(r):
			b *= i + 1
		for i in range(n -r):
			c *= i + 1
		return a/(b*c)

	def generate(self, numRows):
		a = []
		sol = Solution()
		for i in range(5):
			b = []
			for i in range(j):
				b.append(sol.compose(i,j))
			a.append(b)
		return a
