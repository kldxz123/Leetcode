from itertools import combinations
from itertools import product
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        a = [8,4,2,1]
        b = [32,16,8,4,2,1]
        List = []
        for i in range(min(3,num)+1):
        	l = combinations(a,i)
        	m = combinations(b,num - i)
        	sum1 = []
        	sum2 = []
        	tmp = 0
        	for p in l:
        		tmp = sum(p)
        		if tmp < 12:
        			sum1.append(tmp)
        	for p in m:
        		tmp = sum(p)
        		if tmp < 60:
        			sum2.append(tmp)
        	s = product(sum1,sum2)
        	for t in s:
        		if t[1] < 10:
        			string = str(t[0])+":"+"0"+str(t[1])
        		else:
        			string = str(t[0])+":"+str(t[1])
        		List.append(string)
        return List
sol = Solution()
print(sol.readBinaryWatch(2))