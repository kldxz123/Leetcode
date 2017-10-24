
class ListNode(object):
	def __init__(self, x):

		self.val = x
		self.next = None

class Solution(object):
	def removeElements(self, head, val):
		"""
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		pre = ListNode(0)
		pre.next = head
		p = pre
		while head:
			if head.val == val:
				pre.next = head.next
			else:
				pre = head
			head = head.next
		
		return p.next

head = ListNode(0)
p = head
for i in range(6):
	x = ListNode(i+1)
	p.next = x
	p =p.next
p = head.next
'''
while p:
	print(p.val)
	p = p.next
'''
sol = Solution()
b = sol.removeElements(head.next,5)
while b:
	print(b.val)
	b = b.next  