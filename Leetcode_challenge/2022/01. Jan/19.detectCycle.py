'''
142. Linked List Cycle II
Medium

6112

413

Add to List

Share
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        slow, fast = head, head
        entry = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        return None

head = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
tail_connect = 24
# Output: tail connects to node index 24
print(len(head))

dummy = ListNode(0)
curr = dummy
cycle_start = None
count = 0
for i in head:
    curr.next = ListNode(i)
    if count == tail_connect: cycle_start = curr.next
    curr = curr.next
    count += 1
curr.next = cycle_start if cycle_start else None

sol = Solution()
ans = sol.detectCycle(dummy.next)
print(ans.val if ans else ans, cycle_start.val if cycle_start else cycle_start)
