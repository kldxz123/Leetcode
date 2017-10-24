class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ""
        pos = n - 1
        k -= 1
        visited = [0] * n
        while pos >= 1:
        	N = self.getN(pos)
        	mul = int(k/N)
        	rest = k%N
        	
    
    def getN(self,n):
    	tmp = 1
    	while n > 1:
    		tmp *= n
    		n -= 1
    	return tmp

sol = Solution()
print(sol.getPermutation(3,2))