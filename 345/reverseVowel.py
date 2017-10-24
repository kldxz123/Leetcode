class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = []
        b = []
        for c,i in enumerate(s):
        	if i =='a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        		a.append(c)
        		b.append(i)
        b = b[::-1]
        for c,j in enumerate(a):
        	s[j] = b[c]
        return s
sol = Solution()
s = "hello"
print(sol.reverseVowels(s))