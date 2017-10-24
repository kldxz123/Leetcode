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

	def getRow(self, rowIndex):
		a = []
		sol = Solution()
		for i in range(rowIndex + 1):
			a.append(sol.compose(rowIndex,i))
		return a

