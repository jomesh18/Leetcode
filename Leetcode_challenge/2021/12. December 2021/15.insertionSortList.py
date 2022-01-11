'''
147. Insertion Sort List
Medium

Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

    Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
    It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

 

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

 

Constraints:

    The number of nodes in the list is in the range [1, 5000].
    -5000 <= Node.val <= 5000


'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head.next: return head
#         def insert(node, last):
#             dummy = ListNode(0, head)
#             prev = dummy
#             curr = head
#             inserted = False
#             while curr:
#                 if node.val < curr.val:
#                     prev.next = node
#                     node.next = curr
#                     inserted = True
#                     break
#                 prev = curr
#                 curr = curr.next

#             if not inserted:
#                 prev.next = node
#                 last = node
#             return (dummy.next, last)
#         curr = head.next
#         last = head
#         next_start = curr.next
#         while curr:
#             last.next = None
#             head, last = insert(curr, last)
#             last.next = next_start
#             curr = next_start
#             if not curr: break
#             next_start = curr.next
#         return head

#from leetcode, solution
# class Solution:
#     def insertionSortList(self, head: ListNode) -> ListNode:
#         dummy = ListNode()
#         curr = head

#         while curr:
#             # At each iteration, we insert an element into the resulting list.
#             prev = dummy

#             # find the position to insert the current node
#             while prev.next and prev.next.val < curr.val:
#                 prev = prev.next

#             next = curr.next
#             # insert the current node to the new list
#             curr.next = prev.next
#             prev.next = curr

#             # moving on to the next iteration
#             curr = next

#         return dummy.next

#by swapping values
# class Solution:
#     def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         curr = head

#         while curr:
#             j = head
#             while j != curr:
#                 if j.val > curr.val:
#                     j.val, curr.val = curr.val, j.val
#                 j = j.next
#             curr = curr.next
#         return head
