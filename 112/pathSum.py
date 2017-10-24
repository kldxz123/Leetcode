# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def hasPathSum(self,root,sum):
		if root == None:
			return False
		else:
			if sum == root.val and root.right == None and root.left == None:
				return True
			else:
				subSum = sum - root.val
				sol = Solution()
				a = sol.hasPathSum(root.left,subSum)
				b = sol.hasPathSum(root.right,subSum)
				return a or b
