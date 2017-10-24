class Solution(object):
	def titleToNumber(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		#ord('A') = 65
		#chr(65) = 'A'
		t = s[::-1]
		m = 1
		sum = 0
		for i in t:
			tmp = ord(i) - 64
			sum += m*tmp
			m = m*26
		return sum
s = "AZ"
sol = Solution()
print(sol.titleToNumber(s))
