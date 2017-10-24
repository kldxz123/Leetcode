# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
        	return 0
        sol = Solution()
        a = sol.maxDepth(root.left)
        b = sol.maxDepth(root.right)
        if a > b:
        	return a + 1
        else
        	return b + 1

        