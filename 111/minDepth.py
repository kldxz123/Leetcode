# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root == None:
			return 0


		if root.left == None and root.right == None:
			return 1
		sol = Solution()
		if root.left and root.right == None:
			return sol.minDepth(root.left) + 1
		if root.left == None and root.right:

			return sol.minDepth(root.right) + 1
		if root.left and root.right:
			a = sol.minDepth(root.left)
			b = sol.minDepth(root.right)
			if a < b:
				return a + 1
			else:
				return b + 1
        