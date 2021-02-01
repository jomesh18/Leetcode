'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

 class LL:
 	def __init__(self):
 		self.head = None
 	def addAtTail(self, val):
 		node = ListNode(val)
 		if self.head:
 			current = self.head
 			while current.next:
 				current = current.next
 			current.next = node
 		else:
 			self.head = node
 	def __str__(self):
 		l = []
 		current = head
 		while current:
 			l.append(str(current.val))
 		return '==>'.join(l)+'==>'

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
    	current = head
    	while current.val == 6:
    		new_head = current.next
    		current = current.next
    	prev = new_head
    	while current:
    		if current.val == 6:
    			prev.next = current.next
    			current = current.next
    		else:
    			prev = current
    			current = current.next

ll = LL()
for i in range(1, 3):
	ll.addAtTail(i)
ll.addAtTail(6)
for i in range(3, 7):
	ll.addAtTail(i)
s = Solution(ll.head)
