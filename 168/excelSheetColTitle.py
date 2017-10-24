class Solution(object):
	def convertToTitle(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		digit2alpha = ['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
		t = 26
		s = ''
		while n:
			m = n % t
			s += digit2alpha[m]
			n = int(n/t)
			if m == 0:
				n = n - 1

		return s[::-1]

sol = Solution()
print(sol.convertToTitle(28))
