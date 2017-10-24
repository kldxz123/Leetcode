from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = Counter(s)
        for c,i in enumerate(s):
        	if a[i] == 1:
        		return c
        return -1