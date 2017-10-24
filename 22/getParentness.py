class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def subFunction(count_left,count_right,s):
        	if count_left == 0 and count_right == 0:
        		tmp = "("
        		subFunction(count_left + 1, count_right, tmp)
        	if count_left == n and count_right != n:
        		tmp = s + ")"
        		subFunction(count_left,count_right+ 1,tmp)
        	if count_right == n and count_left ==n:
        		result.append(s)
        	if count_left > count_right and count_left < n:
        		tmp = s + "("
        		subFunction(count_left + 1,count_right,tmp)
        		tmp = s + ")"
        		subFunction(count_left,count_right+ 1,tmp)
        	if count_left == count_right:
        		tmp = s + "("
        		subFunction(count_left + 1,count_right,tmp)
        subFunction(0,0,"")
        return result[0:int(len(result)/2)]

sol = Solution()
print(sol.generateParenthesis(4))
