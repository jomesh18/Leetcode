'''
328. Odd Even Linked List
Medium
7K
415
Companies
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
'''
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd, even = head, ListNode(0)
        even_head = even
        curr = head
        odd_prev = None
        while curr and curr.next:
            even.next = curr.next
            even = even.next
            odd.next = curr.next.next
            odd_prev = odd
            odd = odd.next
            curr = odd
        if odd: odd.next = even_head.next
        elif odd_prev: odd_prev.next = even_head.next
        even.next = None
        return head