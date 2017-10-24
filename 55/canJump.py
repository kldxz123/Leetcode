class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        canReach = [[0] * length for i in range(length)]
        #canReach[0][0] = 1

        for i,num in enumerate(nums):
            #canReach[i][i] = 1
            for j in range(num + 1):
                if j < length:
                    canReach[i][i + num] = 1

        index = 1
        
        while index < length:
            





sol = Solution()
a = [3,2,1,0,4]
print(sol.canJump(a))