class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):		
	def sortedArrayToBST(self, nums):
		if nums == []:
			return None
		length = len(nums)
		#print(nums)
		if length % 2 == 1:
			pos = int((length - 1)/2)
			
		else:
			pos = int(length / 2)
		sol = Solution()
		x = TreeNode(nums[pos])
		#print(x.val)
		
		x.left = sol.sortedArrayToBST(nums[0:pos])
		x.right = sol.sortedArrayToBST(nums[pos+1:length])

		return x

		

	def printTree(self, root):
		if root == None:
			return
		else:
			sol = Solution()
			sol.printTree(root.left)
			print(root.val)
			sol.printTree(root.right)


sol = Solution()
a = [1,3,5]
tree = sol.sortedArrayToBST(a)

#sol.printTree(tree)
