class Solution(object):
	def singleNumber(self, nums):
		count = 0
		for i in nums:
			count = count ^ i
		return count



sol = Solution()
a = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]
print(sol.singleNumber(a))
		