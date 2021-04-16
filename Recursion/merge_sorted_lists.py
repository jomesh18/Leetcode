'''
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []

Example 3:

Input: l1 = [], l2 = [0]
Output: [0]

 

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both l1 and l2 are sorted in non-decreasing order.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        def helper(l1, l2, prev):
            if not l1:
                prev.next = l2
                return
            if not l2:
                prev.next = l1
                return
            if l1.val <= l2.val:
                prev.next = l1
                helper(l1.next, l2, prev.next)
            else:
                prev.next = l2
                helper(l1, l2.next, prev.next)
        helper(l1, l2, dummy)
        return dummy.next

#from leetcode
class Solution:        
    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

#from leetcode
# Solution 1

# If both lists are non-empty, I first make sure a starts smaller, use its head as result, and merge the remainders behind it. Otherwise, i.e., if one or both are empty, I just return what's there.

class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b

# Solution 2

# First make sure that a is the "better" one (meaning b is None or has larger/equal value). Then merge the remainders behind a.

class Solution:
    def mergeTwoLists(self, a, b):
        if not a or b and a.val > b.val:
            a, b = b, a
        if a:
            a.next = self.mergeTwoLists(a.next, b)
        return a

def build_list(l):
    if not l: return l
    start = ListNode(l[0])
    prev = start
    for i in l[1:]:
        prev.next = ListNode(i)
        prev = prev.next
    return start

def print_list(l):
    curr = l
    while curr:
        print(curr.val, end='==>')
        curr = curr.next
    print()

l1 = [1,2,4]
l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# l1 = []
# l2 = []
# # Output: []
# l1 = []
# l2 = [0]
# Output: [0]
start1 = build_list(l1)
start2= build_list(l2)
print_list(start1)
print_list(start2)
s = Solution()
start = s.mergeTwoLists(start1, start2)
print_list(start)
# print_list(start1)
# print_list(start2)