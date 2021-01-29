'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

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
		ret = ''
		current = self.head
		while current:
			ret += str(current.val)+ ' ==> '
			current = current.next
		return ret	

class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		current = head
		while current.next:
			current, current.next = current.next, current
			

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL