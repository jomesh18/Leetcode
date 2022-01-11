'''
Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        pos = 0
        while pos != left-1:
            curr = curr.next
            pos += 1
        start = curr
        curr = curr.next
        pos += 1
        stack = []
        while pos != right:
            stack.append(curr)
            curr = curr.next
            pos += 1
        end = curr.next
        start.next = curr
        curr = start.next
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = end
        return dummy.next

def make_ll(head):
    root = ListNode(head[0])
    curr = root
    for val in head[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return root

def print_ll(root):
    curr = root
    res = []
    while curr:
        res.append(curr.val)
        curr = curr.next
    print(res)

head = [1,2,3,4,5]
left = 2
right = 4
# Output: [1,4,3,2,5]

head = [5]
left = 1
right = 1
# Output: [5]

root = make_ll(head)
print_ll(root)
s = Solution()
reversed_ll = s.reverseBetween(root, left, right)
print_ll(reversed_ll)
