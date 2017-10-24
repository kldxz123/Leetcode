class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		pos = 0
		for i in range(len(nums)):
			if nums[i] != 0:
				nums[pos] = nums[i]
				pos += 1
		for i in range(len(nums) - pos):
			nums[pos + i] = 0
		print(nums)

sol = Solution()
a = [0,1,0,3,12]
sol.moveZeroes(a)
        