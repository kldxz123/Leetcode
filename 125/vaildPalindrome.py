import re
class Solution(object):
	def isPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""	
		t = s.lower()
		#print(t)
		a = []
		for i in t:
			if i.isalpha() or i.isdigit():
				a.append(i)
		#print(a)
		b = a[::-1]
		#print(b)
		return a == b
sol = Solution()
a = '0P '
print(sol.isPalindrome(a)) 