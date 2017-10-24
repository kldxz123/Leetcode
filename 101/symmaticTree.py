# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def subTreeSymmetric(self,leftTree,rightTree):
		if leftTree == None and rightTree == None:
			return True
		if leftTree == None or rightTree == None:
			return False
		a = subTreeSymmetric(leftTree.left,rightTree.right)
		b = subTreeSymmetric(leftTree.right,rightTree.left)
		return a and b and leftTree.val == rightTree.val

	def isSymmetric(self, root):
		if root == None:
			return True
		sol = Solution()
		return sol.subTreeSymmetric(root.left,root.right)
        
