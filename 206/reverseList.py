# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		next = ListNode(0)
		pre = None
		while head:
			next = head.next
			head.next = pre
			pre = head
			head = next
		return pre