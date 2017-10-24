from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        flag = 0
        count = Counter(s)
        for i in count:
        	if count[i] % 2 == 0:
        		result += count[i]
        	else:
        		result += int(count[i]/2) * 2
        		flag = 1
        if flag == 1:
        	result += 1
        return result

s = 'ababc'
sol = Solution()
print(sol.longestPalindrome(s))