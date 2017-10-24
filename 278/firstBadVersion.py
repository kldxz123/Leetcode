# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if isBadVersion(1):
		    return 1
		    
		start = 1
		end = n
		
		while start < end:
			a = int((start+end)/2) 
			if isBadVersion(a):
				end = a
			else:
				start = a + 1
		return start
