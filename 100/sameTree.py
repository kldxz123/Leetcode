# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None and q != None) or (p != None and q == None):
        	return False
        else:
        	if p == None and q == None:
        		return True
        	else:
        		leftChild = isSameTree(p.left,q.left)
        		rightChild = isSameTree(p.right,q.right)
        		return leftChild and rightChild and p.val == q.val


        

