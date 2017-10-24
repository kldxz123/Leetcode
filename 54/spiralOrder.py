class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
        	return []

        row_length = len(matrix)
        col_length = len(matrix[0])

        visited = [[0]*(col_length + 1) for i in range(row_length + 1)]
        result = []
        count = 0
        x = 0
        y = 0
        d = 0
        while count < row_length * col_length:
        	result.append(matrix[x][y])
        	visited[x][y] = 1
        	if d == 0:
        		if y == col_length - 1 or visited[x][y + 1] == 1:
        			x += 1
        			d = 1
        		else:
        			y += 1
        	elif d == 1:
        		if x == row_length - 1 or visited[x + 1][y] == 1:
        			y -= 1
        			d = 2
        		else:
        			x += 1
        	elif d == 2:
        		if y == 0 or visited[x][y - 1] == 1:
        			x -= 1
        			d = 3
        		else:
        			y -= 1
        	else:
        		if x == 0 or visited[x- 1][y] == 1:
        			y += 1
        			d = 0
        		else:
        			x -= 1

        	count += 1
        return result
sol = Solution()
a = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
 [ 10, 11, 12 ]
]
print(sol.spiralOrder(a))