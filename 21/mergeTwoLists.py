# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

def mergeTwoLists(l1, l2):
	p = first = ListNode(0)
	
	while(l1 and l2):
		if l1.val < l2.val:
			p.next = l1
			l1 = l1.next
			p = p.next
		else:
			p.next = l2
			l2 = l2.next
			p = p.next
	if l1:
		p.next = l1
	else:
		p.next = l2
	return first.next

l1 = ListNode(1)
l2 = ListNode(2)
merge = mergeTwoLists(l1,l2)
while merge:
	print(merge.val)
	merge = merge.next

