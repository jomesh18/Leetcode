'''
Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

 

Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list(li):
    if not li: return li
    start = ListNode(li[0])
    curr = start
    for i in range(1, len(li)):
        curr.next = ListNode(li[i])
        curr = curr.next
    return start

def print_ll(head):
    curr = head
    while curr:
        print(curr.val, end='==>')
        curr = curr.next

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         def helper(prev, head):
#             if not head: return prev
#             n = head.next
#             head.next = prev
#             return helper(head, n)
#         return helper(None, head)
        
#from leetcode solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
ll_head = create_list(head)
print_ll(ll_head)
print()
s = Solution()
print_ll(s.reverseList(ll_head))
print()
