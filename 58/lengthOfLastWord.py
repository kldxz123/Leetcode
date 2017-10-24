import re
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        count = 0
        lastCount = 0
        for i in s:
        	if i == " ":
        		if count != 0:
        			lastCount = count 
        			count = 0
        	else:
        		count = count + 1
       	if count != 0:
       		lastCount = count
       	return lastCount

sol = Solution()
s = "b  c  "
print(sol.lengthOfLastWord(s))
        