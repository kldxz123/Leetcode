from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = Counter(s)
        #print(a)
        b = Counter(t)
        #print(b)
        for i in b:
        	print(i)
        	if a.get(i) is None:
        		return i
        	if b[i] != a[i]:
        		return i

s = 'abcd'
t = 'abcde'
sol = Solution()
print(sol.findTheDifference(s,t))