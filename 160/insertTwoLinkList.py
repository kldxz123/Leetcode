# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def getIntersectionNode(self, headA, headB):
		"""
		:type head1, head1: ListNode
		:rtype: ListNode
		"""
		p = headA
		q = headB
		if p == None or q == None:
			return None
		len1 = 0
		len2 = 0
		while p:
			len1 += 1
			p = p.next
		while q:
			len2 += 1
			q = q.next
		p = headA
		q = headB
		while len1-len2:
			p = p.next
			len1 -= 1
		while len2 - len1:
			q = q.next
			len2 -= 1
		while q != p
			p = p.next
			q = q.next
		return q
