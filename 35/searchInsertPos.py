class Solution(object):
	def searchInsert(self, nums, target):
		count=0
		for i in nums:
			if target > i:
				count += 1
			else:
				return count
		return count
sol = Solution()
nums = [1,3,5,6]
print(sol.searchInsert(nums,7))