class Solution(object):
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		sum = 0
		for i in nums:
			sum = sum + i
		n = len(nums)
		return int(n*(n+1)/2 - sum)

a = [0,1,2]
sol = Solution()
print(sol.missingNumber(a))
