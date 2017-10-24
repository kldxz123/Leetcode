class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 2
        while num >= i:
        	i = i * 2
        return i - 1 - num 
sol = Solution()
print(sol.findComplement(4))