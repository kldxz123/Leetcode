class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0;
        for i,c in enumerate(grid):
        	for j,g in enumerate(c):
        		if g == 1:
        			temp = 4
        			if i - 1 >= 0 and grid[i - 1][j] == 1:
        				temp -= 2
        			if j - 1 >= 0 and grid[i][j - 1] == 1:
        				temp -= 2
        			count += temp
        			print(count)
        return count

sol = Solution()
grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
print(sol.islandPerimeter(grid))