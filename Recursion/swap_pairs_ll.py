'''
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

 

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]

 

Constraints:

    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100

 
Follow up: Can you solve the problem without modifying the values in the list's nodes? (i.e., Only nodes themselves may be changed.)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            next_start = head.next.next
            head.next.next = head
            head = head.next
        else:
            return head
        head.next.next = self.swapPairs(next_start)
        return head

#from leetcode
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_start)
        return head

#fromm leetcode
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return second

def build_ll(head):
    if not head: return head
    start = ListNode(head[0])
    curr = start
    for i in range(1, len(head)):
        curr.next = ListNode(head[i])
        curr = curr.next
    return start

def print_ll(head):
    curr = head
    ref = []
    while curr:
        ref.append(curr)
        print(curr.val, sep="==>", end=" ")
        curr = curr.next
    return ref

head = [1,2,3,4]
# Output: [2,1,4,3]
head = []
# Output: []
head = [1]
# Output: [1]
print('Input = {}'.format(head))
start = build_ll(head)
print('LL')
ref = print_ll(start)
print(ref)
print()
s = Solution()
swapped = s.swapPairs(start)
print('After pair swap')
swap_ref = print_ll(swapped)
print(swap_ref)
print()
