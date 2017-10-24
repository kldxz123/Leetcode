class Solution(object):
	def compose(self,n,r):
		a = 1
		b = 1
		c = 1
		if r == 0:
			return 1

		for i in range(n):
			a *= i + 1
		for i in range(r):
			b *= i + 1
		for i in range(n-r):
			c *= i + 1
		return a/(b*c)

	def climbStairs(self, n):
		sol = Solution()
		sum = 0
		if n%2 == 0:
			for i in range(int(n/2)+1):
				sum += sol.compose(n-i, i)
		else:
			for i in range(int((n-1)/2)+1):
				sum += sol.compose(n-i,i)
		return int(sum)

    
sol = Solution()
print(sol.climbStairs(3))
