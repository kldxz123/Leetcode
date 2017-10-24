class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        a = [0]*len(nums)
        for i in nums:
        	if a[i] == 0:
        		a[i] = 1
        for c,i in enumerate(a):
        	if  i == 0:
        		result.append(c + 1)