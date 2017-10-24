class Solution(object):
	def isIsomorphic(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		a = {}
		if len(s) != len(t):
			return False
		for i in range(len(s)):
			if a.get(s[i]) == None:
				a[s[i]] = t[i]
			else:
				if a[s[i]] != t[i]:
					return False
		return True
sol = Solution()
s = "aa"
t = "aa"
print(sol.isIsomorphic(s,t))
