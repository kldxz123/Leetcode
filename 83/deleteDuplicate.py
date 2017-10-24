# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
        	return head
        before = ListNode(head.val - 1)
        t = before
        before.next = head
        while head:
        	if head.val != before.val:
        		before = before.next
        		head = head.next
        	else:
        		before.next = head.next
        		head = head.next
        return t.next



