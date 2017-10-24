class Solution(object):
	def wordPattern(self, pattern, str):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""
		s = str.split()
		if len(s) != len(pattern):
			return False
		dict = {}
		for count,i in enumerate(pattern):
			if dict.get(i) == None:
				dict[i] = s[count]
			else:
				if dict[i] != s[count]:
					return False
		dict2={}
		for count,i in enumerate(s):
			if dict2.get(i) == None:
				dict2[i] = pattern[count]
			else:
				if dict2[i] != pattern[count]:
					return False

		return True

pattern = "abba"
str = "I I I I"

sol = Solution()
print(sol.wordPattern(pattern,str)) 
