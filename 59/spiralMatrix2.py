class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if num == 0:
        	return []
        num = n * n
        result = []
        
        result.append([num])
        r = 1
        num -= 1
        while num > 0:
        	count = 0
        	tmp = []
        		tmp.append(num)
        		num -= 1
        		count += 1
        	result.append(tmp)
        	result = list(zip(*result[::-1]))
        	r = len(result[0])

        result = list(zip(*result[::-1]))
        return result
sol = Solution()
print(sol.generateMatrix(4))