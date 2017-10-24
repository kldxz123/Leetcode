class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort(reverse = False)

        result = []

        def findNext(index,target,lastList):
        	tmp = target - candidates[index]
        	if tmp == 0:
        		newList = lastList + [candidates[index]]
        		if newList not in result:
        			result.append(newList)
        		if index > 0:
        			findNext(index - 1,target,lastList)
        	elif tmp < 0:
        		if index > 0:
        			findNext(index - 1,target,lastList)
        		else:
        			return 
        	else:
        		newList = lastList + [candidates[index]]
        		if index > 0:
        			findNext(index - 1,tmp,newList)
        		if index > 0:
        			findNext(index - 1,target,lastList)
        index = len(candidates) - 1
        lastList = []
        findNext(index,target,lastList)
        print(result)
        return result

sol = Solution()
sol.combinationSum2([1,2],5)