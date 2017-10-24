from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a = Counter(ransomNote)
        b = Counter(magazine)
        for i in a:
        	if i in b:
        		if a[i] > b[i]:
        			return False
        	else:
        		return False
        return True