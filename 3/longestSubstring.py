#3. Longest Substring Without Repeating Characters 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        l = {}
        max_count = 0
        length = 0
        for c,i in enumerate(s):
        	if i not in l:
        		l[i] = 1
        		length += 1
        	else:
        		if l[i] == 0:
        			l[i] = 1
        			length += 1
        		else:
        			while s[start] != i:
        				l[s[start]] = 0
        				start += 1
        				length -= 1
        			start += 1

        	if length > max_count:
        		max_count = length

        return max_count

sol = Solution()
print(sol.lengthOfLongestSubstring("bpfbhmipx"))