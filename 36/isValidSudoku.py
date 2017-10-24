class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        
        """
        def testRow():
        	for row in board:
        		tmp = []
        		for i in row:
        			if i not in tmp:
        				tmp.append(i)
        			else:
        				if i != ".":
        					return False
        	return True

        def testCol():
        	for j in range(9):
        		tmp = []
        		for i in range(9):
        			if board[i][j] not in tmp:
        				tmp.append(board[i][j])
        			else:
        				if board[i][j] != ".":
        					return False
        	return True

        def testSquare():
        	centers = [[1,1],[1,4],[1,7],[4,1],[4,4],[4,7],[7,1],[7,4],[7,7]]
        	for center in centers:
        		tmp = []
        		for i in range(-1,2):
        			for j in range(-1,2):
        				if board[center[0] + i][center[1] + j] not in tmp:
        					tmp.append(board[center[0] + i][center[1] + j])
        				else:
        					if board[center[0] + i][center[1] + j] != ".":
        						return False
        	return True
        return testSquare() and testCol() and testRow()

