'''
  Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

 

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

 

Constraints:

	The number of nodes in the list is sz.
	1 <= sz <= 30
	0 <= Node.val <= 100
	1 <= n <= sz


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
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		if n == 1:
			head.val = None
		fast = head
		slow = head
		i = 0
		while i < n and fast.next:
			i += 1
			fast = fast.next
		while fast.next:
			fast = fast.next
			slow = slow.next
		if slow.next:
			slow.next = slow.next.next
		return head

ll = LL()
head = [1,2,3,4,5]
n = 2
# Output: [1,2,3,5]
head = [1]
n = 1
# Output: []
head = [1,2]
n = 1
# Output: [1]
for i in head:
	ll.addAtTail(i)
print(ll)
s = Solution()
s.removeNthFromEnd(ll.head, n)
print(ll)
