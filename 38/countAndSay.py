class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n - 1):
        	t = ''
        	a = s[0]
        	count = 0
        	for j in s:
        		if a == j:
        			count += 1
        		else:
        			t = t + str(count)
        			t = t + str(a)
        			count = 1
        			a = j
        	t = t + str(count)
        	t = t + str(a)
        	s = t
        return s 
sol = Solution()
print(sol.countAndSay(6))

