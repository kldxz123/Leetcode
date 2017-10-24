# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		if head == None:
			return True
		num = []
		while head:
			num.append(head.val)
			head = head.next
		p = num[::-1]
		if p == num:
			return True
		else:
			return False
        