'''
143. Reorder List
Medium

4545

184

Add to List

Share
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         def print_list(node):
#             res = []
#             curr = node
#             while curr:
#                 res.append(curr.val)
#                 curr = curr.next
#             return res

#         def reverse(curr):
#             if not curr.next:
#                 self.second_list = curr
#                 return curr
#             next_ = reverse(curr.next)
#             print(curr.val)
#             next_.next = curr
#             return curr
        
#         #finding number of node in list
#         n = 0
#         curr = head
#         while curr:
#             n += 1
#             curr = curr.next
#         if n<3: return head
#         #dividing list as two
#         divide = (n-1)>>1
#         divide_start = n - divide

#         # finding starting of second list
#         curr = head
#         count = 0
#         prev = None
#         while count < divide_start:
#             prev = curr
#             curr = curr.next
#             count += 1
#         prev.next = None
#         print(print_list(head), print_list(curr))
#         #reversing second list
#         dummy = ListNode(0, curr)
#         self.second_list = None

#         reverse(curr).next = None
#         dummy.next.next = None
#         print(print_list(self.second_list))

#         #inserting second_list inbetween first_list
#         second_list = self.second_list    
#         first_list = head

#         while first_list and second_list:
#             temp = first_list.next
#             first_list.next = second_list
#             temp2 = second_list.next
#             second_list.next = temp
#             first_list = temp
#             second_list = temp2
#         return head

#using extra space
# class Solution:
#     def reorderList(self, head):
#         arr, Iter = [], head
#         while Iter:
#             arr.append(Iter)
#             Iter = Iter.next
#         # print([i.val for i in arr])
#         L, R = 1, len(arr)-1
#         for i in range(len(arr)):
#             if i & 1:
#                 head.next = arr[L]
#                 L += 1
#             else:
#                 head.next = arr[R]
#                 R -= 1
#             print(head.val, head.next.val)
#             head = head.next
#         head.next = None


class Solution:
    def reorderList(self, head):
        # finding the mid point
        def find_mid(head):
            fast, slow = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def find_reverse(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev, node = node, next_node
            return prev

        if not head or not head.next: return
        L, R, i = head.next, find_reverse(find_mid(head)), 0
        while L != R:
            if i&1:
                head.next = L
                L = L.next
            else:
                head.next = R
                R = R.next
            head = head.next
            i += 1

def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

dummy = ListNode(0)
prev = dummy
for i in range(1, 4):
    node = ListNode(i)
    prev.next = node
    prev = node

head = dummy.next
print(print_list(head))
sol = Solution()
print(sol.reorderList(head))
print(print_list(head))
