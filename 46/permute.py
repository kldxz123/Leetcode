class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
        	tmp = []
        	for x in result:
        		for i in range(len(x) + 1):
        			tmp.append(x[:i] + [num] + x[i:])
        	result = tmp
        return result



    



sol = Solution()
print(sol.permute([1,2,3,4]))