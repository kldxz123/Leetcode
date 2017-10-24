class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = -999999999999
        tempSum = 0
        for i in nums:
        	if tempSum > 0:
        		tempSum += i
        	else:
        		tempSum = i
        	if tempSum > maxSum:
        		maxSum = tempSum
        return maxSum

sol = Solution()
nums = [-2,-1]
print(sol.maxSubArray(nums))
