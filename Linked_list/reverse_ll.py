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
		first = head
		while first.next:
			second = first.next
			first.next = second.next
			second.next = head
			head = second
		return head

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

ll = LL()
input_l = [1, 2, 3, 4, 5]
for i in input_l:
	ll.addAtTail(i)
print(ll)
s = Solution()
# reverse_ll = s.reverseList(ll.head)
# current = reverse_ll
# st = ''
# while current:
# 	st += str(current.val)+ ' ==> '
# 	current = current.next
# print(st)
reverse_ll = LL()
reverse_ll.head = s.reverseList(ll.head)
print(reverse_ll)
