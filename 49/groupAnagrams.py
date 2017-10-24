import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictionary = {}
        result = []
        count = 0
        for string in strs:
        	tmp = "".join((lambda x:(x.sort(),x)[1])(list(string)))
        	#print(tmp)
        	if tmp not in dictionary:
        		tmpList = [string]
        		result.append(tmpList)
        		dictionary[tmp] = count 
        		count += 1
        	else:
        		index = dictionary[tmp]
        		result[index].append(string)
        #print(dictionary)
        return result
sol = Solution()
array = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(array))
        