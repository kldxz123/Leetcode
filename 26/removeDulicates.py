class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
        	return 0
        a = nums[0]
        count = 1
        j = 1
        for i in nums:
        	if i == a:
        		continue
        	else:
        		count = count + 1
        		nums[j] = i
        		j = j + 1
        		a = i
        print(nums[0:count])
        return count

nums = [1,1,2,2,3]
sol = Solution()
print(sol.removeDuplicates(nums))

