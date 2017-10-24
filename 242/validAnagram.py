class Solution(object):
	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if len(s) != len(t):
			return False
		dict = {}
		for c in s:
			if dict.get(c) == None:
				dict[c] = 1
			else:
				dict[c] += 1
		for c in t:
			if dict.get(c) != None:
				dict[c] -= 1
				if dict[c] < 0:
				    return False
			else:
				return False
		return True