class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        if len(s) < 3:
        	return max(s)
        s = s - {max(s)}
        s = s - {max(s)}
        return max(s)


sol = Solution()
nums = [14,5,2,1,5]
print(sol.thirdMax(nums))