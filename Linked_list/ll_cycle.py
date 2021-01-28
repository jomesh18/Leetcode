'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

 

Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         current = head
#         visited = set()
#         while current:
#             if current in visited:
#                 return True
            # visited.append(current)
            # current = current.next
#         return False

 # from leetcode

 #Floyd's technique

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def addAtTail(self, val):
        node = ListNode(val)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def __str__(self):
        ret = ''
        current = self.head
        while current:
            ret += str(current.val)+ ' ==> '
            current = current.next
        return ret

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
    	if head is None:
    		return False
    	slow = head
    	fast = head.next
    	while slow != fast:
    		if fast is None or fast.next is None:
    			return False
    		slow = slow.next
    		fast = fast.next.next
    	return True

# head = [3,2,0,-4]
# pos = 1
head = [1]
pos = -1
ll = LL()
for i in head:
    ll.addAtTail(i)
print(ll)
if pos != -1:
    current = ll.head
    i = 0
    while i != pos:
        current = current.next
        i += 1
    cycle_start = current
    while current.next:
        current = current.next
    current.next = cycle_start
i = 0
current = ll.head
ret = ''
while(i<10 and current):
    i += 1
    ret += str(current.val)+ ' ==> '
    current = current.next
print(ret)
 # Output: true

obj = Solution()
print(obj.hasCycle(ll.head))
