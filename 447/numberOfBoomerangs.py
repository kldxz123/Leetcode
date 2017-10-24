from collections import Counter
class Solution(object):
    def p(self,n,r):
        if n ==0 or r == 0:
        	return 1
        a = 1
        for i in range(n-r):
        	a *= i + 1
        b = 1
        for i in range(n):
        	b *= i + 1
      
        return b/a

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sum = 0
        size = len(points)
        dist = []
        for i in points:
        	for j in points:
        		dist.append((i[0] - j[0])*(i[0] - j[0]) + (i[1] - j[1])*(i[1] - j[1]))
        	d = Counter(dist)
        	for k in d:
        		if k != 0:
        			count = d[k]
        			if count >= 2:
        				sum += self.p(count,2)
        	dist = []
        return sum

sol = Solution()
points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
print(sol.numberOfBoomerangs(points))