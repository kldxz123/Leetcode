#5. Longest Palindromic Substring 

class Solution(object):
    def getLongestSubstring(self,s):
    	if len(s) == 1:
    		return s
    	if len(s) == 2:
    		if s[0] == s[-1]:
    			return s
    		else:
    			return ""
    	if s[0] == s[-1]:
    		if self.getLongestSubstring(s[1:-1]) != "":
    			return s
    		else:
    			return s[0]
    	else:
    		if self.getLongestSubstring(s[0:-1]) != "":
    			return s[0:-1]
                
    		else:
    			if self.getLongestSubstring(s[1:]) != "":
    				return s[1:]
    			else:
    				return s[0]
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.getLongestSubstring(s)
        


sol = Solution()
print(sol.longestPalindrome("babad"))
#print(s[-1])