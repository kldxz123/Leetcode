class Solution(object):
    def permuteUnique(self, nums):
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
        			if i < len(x) and x[i] == num:
        				break
        	result = tmp
        return result