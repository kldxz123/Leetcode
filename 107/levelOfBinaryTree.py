class TreeNode(object):
    def __init__(self, x):
        self.val = x         
        self.left = None
        self.right = None

class Solution(object):
	def findNextLevel(self,l):
		a = []
		for i in l:
			if i.left:
				a.append(i.left)
			if i.right:
				a.append(i.right)
		return a
	def levelOrderBottom(self, root):
		sol = Solution()
		a = []
		c = []
		d = []
		if root == None:
			return a
		a.append(root)
		while a:        	
			for i in a:
				c.append(i.val)

			d.append(c)
			b = sol.findNextLevel(a)
			a = b
			c = []
		return d[::-1]

a1 = TreeNode(3)
a2 = TreeNode(9)
a3 = TreeNode(20)
a4 = TreeNode(15)
a5 = TreeNode(7)
a1.left = a2
a1.right = a3
a3.left = a4
a3.right = a5
sol = Solution()
print(sol.levelOrderBottom(a1))

        
