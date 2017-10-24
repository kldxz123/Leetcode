class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        result = []
        if length < 4:
        	return result
        for i in range(length - 3):
        	#if i > 0 and nums[i] == nums[i - 1]:
        		#continue
        	tempSum = target - nums[i]
        	for j in range(i + 1, length - 2):
        		#if j > i and nums[j] == nums[j - 1]:
        			#continue
        		nextSum = tempSum - nums[j]

        		l = j + 1
        		r = length -1
        		while l < r:
        			if nums[l] + nums[r] < nextSum:
        				l += 1
        			elif nums[l] + nums[r] > nextSum:
        				r -= 1
        			else:
        				if [nums[i],nums[j],nums[l],nums[r]] not in result:
        					result.append([nums[i],nums[j],nums[l],nums[r]])
        				'''
        				while l < r and nums[l] == nums[l + 1]:
        					l += 1
        				while l < r and nums[r] == nums[r - 1]:
        					r -= 1
        				'''
        				l += 1
        				r -= 1
        return result

sol = Solution()
print(sol.fourSum([0,0,0,0],0))