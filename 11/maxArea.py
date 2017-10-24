class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        max_area = 0
        while start <= end:
        	if height[start] < height[end]:
        		area = (end - start) * height[start]
        		start += 1
        	else:
        		area = (end - start) * height[end]
        		end -= 1
        	#print(area)
        	if area > max_area:
        		max_area = area
        return max_area

sol=Solution()
a = [1,1]
print(sol.maxArea(a))