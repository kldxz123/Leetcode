class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort(reverse = False)

        result = []

        def findNext(index,target,forwardList):
        	
        	tmp = target - candidates[index]
        	#print("index:",index,"target:",target,"forwardList:",forwardList,"tmp:",tmp,"Result:",result)
        	if tmp == 0:
        		newList = forwardList + [target]
        		result.append(newList)
        		if index != 0:
        			findNext(index - 1,target,forwardList)
        	elif tmp < 0:
        		if index == 0:
        			return None
        		else:
        			findNext(index - 1,target,forwardList)
        	else:
        		newList = forwardList + [candidates[index]]
        		findNext(index,tmp,newList) 
        		if index > 0:

        			findNext(index - 1,target,forwardList)

        
        index = len(candidates) - 1
        forwardList = []
        findNext(index,target,forwardList)
        return result

sol = Solution()
print(sol.combinationSum([2, 3, 6, 7],7))

