# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
        	return head
        def changeFirstTwo(h):
        	if h == None:
        		return h
        	elif h.next == None:
        		return h
        	else:
        		a = changeFirstTwo(h.next.next)
        		tmp = ListNode(0)
        		tmp.next = h.next
        		h.next = h.next.next
        		tmp.next.next = h
        		tmp.next.next.next = a
        		return tmp.next
            
        tmp = changeFirstTwo(head)
        return tmp