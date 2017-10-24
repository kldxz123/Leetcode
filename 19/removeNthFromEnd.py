# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def index(head):
        	if head == None:
        		return 0
        	i = index(head.next) + 1
        	if i > n:
        		head.next.val = head.val
        	return i
        index(head)
        return head.next