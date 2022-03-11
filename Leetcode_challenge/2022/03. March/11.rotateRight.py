'''
61. Rotate List
Medium

4672

1257

Add to List

Share
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
Accepted
521,867
Submissions
1,513,203
Seen this question in a real interview before?

Yes

No
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        l = 0
        curr = head
        prev = None
        while curr:
            prev = curr
            curr = curr.next
            l += 1
        k %= l
        prev.next = head
        curr = head
        prev = None
        i = 0
        while i < l-k-1:
            i += 1
            curr = curr.next
        head = curr.next
        curr.next = None
        return head
        