class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = []
        
        length = len(nums)
        if length < 3:
        	return result
        minDis = 100000000000
        nums.sort()
        for i in range(length - 2):
        	l = i + 1
        	r = length - 1
        	while l < r:
        		s = nums[i] + nums[l] + nums[r]
        		tmpDis = s - target
        		if tmpDis == 0:
        			return target
        		if abs(tmpDis) < abs(minDis):
        				minDis = tmpDis
        		if tmpDis > 0:
        			r -= 1
        			continue
        		elif tmpDis < 0:
        			l += 1
        			continue
        return target + minDis
sol = Solution()
array = [-1,2,1,-4]
print(sol.threeSumClosest(array,1))