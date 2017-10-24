class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
        	i -= 1
        print(i)
        if i == 0:
        	nums.reverse()
        
        else:
        	j = len(nums) - 1
        	while j >= i and nums[j] <= nums[i-1]:
        		j -= 1
        	print(i,j)
        	tmp = nums[i - 1]
        	nums[i-1] = nums[j]
        	nums[j] = tmp
        	x = nums[i:len(nums)]
        	x.reverse()
        	print(x)
        	for k in range(i,len(nums)):
        		nums[k] = x[k - i]

        print(nums)
        

sol = Solution()
sol.nextPermutation([5,1,1])
