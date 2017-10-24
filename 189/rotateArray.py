class Solution(object):
	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: void Do not return anything, modify nums in-place instead.
		"""

		p = len(nums)
		k = k % p
		print(k)
		nums = nums[p-k:p+p-k] + nums[0:p - k]
		return nums

a = [1,2]

sol = Solution()
print(sol.rotate(a,1))
