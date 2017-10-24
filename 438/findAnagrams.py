from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        '''
        List = []
        l = len(p)
        p_count = Counter(p)
        for i in range(len(s) - l + 1):
        	tmp = s[i:i + l]
        	tmp_count = Counter(tmp)
        	if p_count == tmp_count:
        		List.append(i)
        return List
        '''
        List = []
        i = 0
        j = 0
        p_count = Counter(p)
        tmp = {}
        len_s = len(s)
        len_p = len(p)
        while j < len_s:
        	a = s[j]
        	if p_count.get(a) != None:
        		if tmp.get(a) != None:





sol = Solution()
s = "abab"
p = "ab"
print(sol.findAnagrams(s,p))