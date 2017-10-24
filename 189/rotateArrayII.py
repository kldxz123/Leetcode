class Solution(object):
	def rotate(self,nums,k):
		nums = nums[0:len(nums)-k:-1]
		print
		nums = nums[len(nums)-k+1:len(nums):-1]
		nums = nums[::-1]
		return nums

	def reverse(self,nums,start,end)
		nums
sol = Solution()
a = [1,2,3,4,5,6,7]
print(sol.rotate(a,3))