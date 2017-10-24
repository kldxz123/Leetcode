# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def getDepth(self,root):
		if root == None:
			return 0
		sol = Solution()
		a = sol.getDepth(root.left)
		b = sol.getDepth(root.right)
		
		if a > b:
			return a + 1
		else:
			return b + 1

	def isBalanced(self, root):
		if root == None:
			return True
		sol = Solution()
		a = sol.getDepth(root.left)
		b = sol.getDepth(root.right)
		if a - b <= 1 and b - a <= 1:
			c = True
		return c and sol.isBalanced(root.left) and sol.isBalanced(root.right)
