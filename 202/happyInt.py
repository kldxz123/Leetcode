class Solution(object):

	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		t = [True,False,False,False,False,False,True,False,False]
		if n > 0 and n < 10:
			return t[n - 1]
		p = str(n)
		sum = 0
		for i in p:
			x = int(i)*int(i)
			sum += x
		return self.isHappy(sum)

sol = Solution()
print(sol.isHappy(68))
        