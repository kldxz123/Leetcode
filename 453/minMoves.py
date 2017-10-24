class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = sorted(nums)
        s = 0
        tmp = num[0]
        i = 1
        while i <len(nums) and num[i] == tmp:
        	i += 1
        if i == len(nums):
        	return 0
        while i < len(num) - 1:
        	s += num[i] - num[0]
        	i += 1
        after = (num[-1] + s)*len(nums)

        return int((after - sum(nums))/(len(nums) - 1))
sol = Solution()
nums = [1,1,1]
print(sol.minMoves(nums))