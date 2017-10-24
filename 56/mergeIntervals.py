# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x:x.start)
        result = []

        i = 0
        while i < len(intervals):
        	tmp = intervals[i]
        	j = 1
        	while i+j <= len(intervals) - 1 and tmp.end >= intervals[i+j].start:
        		if tmp.end < intervals[i+j].end:
        			tmp.end = intervals[i + j].end
        		j += 1
        	result.append(tmp)
        	i += j

        return result

sol = Solution()
intervals = [[1,3],[8,10],[2,6],[15,18]]
print(sol.merge(intervals))
        		


