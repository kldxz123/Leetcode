class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        c = x ^ y
        d = bin(c)

        count = 0
        for i in d:
        	if i == '1':
        		count += 1
        return count
sol = Solution()
print(sol.hammingDistance(1,4))