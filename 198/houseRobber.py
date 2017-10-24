class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0:
		    return 0
		no = 0
		sum = nums[0]
		pre = nums[0]
		for i in range(len(nums) - 1):
			tmp = nums[i + 1] + no
			no = sum
			if tmp > sum:
				sum = tmp
			
		return sum 
sol = Solution()
num = [3,7,2,4,5,1,6,8]
print(sol.rob(num))
