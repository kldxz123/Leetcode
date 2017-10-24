class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in nums:
        	if i == val:
        		continue
        	else:
        		nums[j] = i
        		j = j + 1
        		
        	
        print(nums)
        return j
sol = Solution()
y = [2,3,3,2]
print(sol.removeElement(y,3))

