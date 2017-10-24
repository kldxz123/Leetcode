from functools import reduce
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = {'0':[" "],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['q','p','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        if digits == "":
        	return []
        else:
        	a = reduce(lambda result,digit:[x+y for x in result for y in letters[digit]],digits,[''])
        return a
sol = Solution()
digits = '23'
print(sol.letterCombinations(digits))
          