# 2. add two numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x = l1
        y = l2
        a = 0
        result = ListNode()
        pos = result
        while x != None and y != None:
        	tmp = x.val + y.val + a
        	if tmp < 10:
        		a = 0
        		b = tmp
        	else:
        		a = 1
        		b = tmp % 10
        	temp_node = ListNode()
        	temp_node.val = b
        	pos.next = temp_node
        	pos = pos.next
        	x = x.next
        	y = y.next
        if x != None:
        	rest = x
        else:
        	if y != None:
        		rest = y
        if rest != None:
        	while a == 1 and rest:
        		tmp = a + rest.val
        		if tmp >= 10:
        			a = 1
        			b = tmp % 10
        		else:
        			a = 0
        			b = tmp
        		temp_node = ListNode()
        		temp_node.val = b
        		pos.next = temp_node
        		pos = pos.next
        		rest = rest.next
        	if a == 1:
        		temp_node = ListNode()
        		temp_node.val = 1
        		pos.next = temp_node
        	else:
        		pos.next = rest
        return result

        