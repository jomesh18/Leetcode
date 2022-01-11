'''
Palindrome Linked List

Solution
Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#O(n) time, O(n) space
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next
#         return arr == arr[::-1]

#O(n) time, O(n) space
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         self.front_pointer = head
#         def recursive_helper(node):
#             if not node: return True
#             if not recursive_helper(node.next): return False
#             if self.front_pointer.val != node.val: return False
#             self.front_pointer = self.front_pointer.next
#             return True
#         return recursive_helper(head)

#O(n) time, O(1) space
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return True

        #fn to find the start of second list
        def find_mid(head):
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        mid = find_mid(head)
        second_list_start = mid.next
        mid.next = None

        #fn to reverse the list
        def reverse_list(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev

        reversed_second_list = reverse_list(second_list_start)

        #compare first and second half
        def compare_l1_l2(l1, l2):
            while l1 and l2:
                if l1.val != l2.val: return False
                l1 = l1.next
                l2 = l2.next
            return True
        is_palin = compare_l1_l2(head, reversed_second_list)
        
        # restore the second half (reverse and connect)

        mid.next = reverse_list(reversed_second_list)

        return is_palin


#from leetcode solution (by Hai_dee) (always clear detailed solutions)
# class Solution:

#     def isPalindrome(self, head: ListNode) -> bool:
#         if head is None:
#             return True

#         # Find the end of first half and reverse second half.
#         first_half_end = self.end_of_first_half(head)
#         second_half_start = self.reverse_list(first_half_end.next)

#         # Check whether or not there's a palindrome.
#         result = True
#         first_position = head
#         second_position = second_half_start
#         while result and second_position is not None:
#             if first_position.val != second_position.val:
#                 result = False
#             first_position = first_position.next
#             second_position = second_position.next

#         # Restore the list and return the result.
#         first_half_end.next = self.reverse_list(second_half_start)
#         return result    

#     def end_of_first_half(self, head):
#         fast = head
#         slow = head
#         while fast.next is not None and fast.next.next is not None:
#             fast = fast.next.next
#             slow = slow.next
#         return slow

#     def reverse_list(self, head):
#         previous = None
#         current = head
#         while current is not None:
#             next_node = current.next
#             current.next = previous
#             previous = current
#             current = next_node
#         return previous


head = [1,2]
# Output: False

sol = Solution()
print(sol.isPalindrome(head))
