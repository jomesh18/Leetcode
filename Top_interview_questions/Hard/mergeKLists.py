'''
Merge k Sorted Lists

Solution
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while any(lists):
            t = ListNode(float('inf'))
            pos = 0
            for i in range(len(lists)):
                if lists[i] and lists[i].val < t.val:
                    t, pos = lists[i], i
            curr.next = t
            curr = curr.next
            lists[pos] = t.next
        return dummy.next


#sort, nlogn
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        s = []
        for l in lists:
            while l:
                s.append(l.val)
                l = l.next
        s.sort()
        dummy = curr = ListNode()
        for v in s:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

#using heaps
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        curr = dummy = ListNode()
        for i, l in enumerate(lists):
            if l:
                heappush(heap, (l.val, i, l))
        while heap:
            val, i, node = heappop(heap)
            curr.next, node = node, node.next
            curr = curr.next
            if node: heappush(heap, (node.val, i, node))
        return dummy.next


#using divide and conquer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        interval = 1
        while interval < k:
            for i in range(0, k-interval, interval*2):
                lists[i] = self.merge2(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if k else None
    def merge2(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
        