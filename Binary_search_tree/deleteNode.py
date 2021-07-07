'''
Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

    Search for a node to remove.
    If the node is found, delete the node.

Follow up: Can you solve it with time complexity O(height of tree)?

 

Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:

Input: root = [], key = 0
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -105 <= Node.val <= 105
    Each node has a unique value.
    root is a valid binary search tree.
    -105 <= key <= 105

'''

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        curr = root
        pos = None
        while curr:
            pos = curr
            if key > curr.val:
                curr = curr.right
            elif key < curr.val:
                curr = curr.left
            else:
                break
        def inorderSuccessor(curr):
            node = root
            succ = None
            while node:
                if node.val <= curr.val:
                    node = node.right
                else:
                    succ = node
                    node = node.left
            prev = None
            node = root
            if node != succ:
                while node:
                    if node.left = succ:
                        node.left = None
                    elif node.right = succ:
                        node.right = None
                    elif node.right.val > succ.val:

            return succ

        inorderSuccessor(curr)


def build_tree(root):
    start = TreeNode(root[0])
    q = deque([start])
    i = 1
    while i<len(root):
        curr = q.popleft()
        if curr:
            curr.left = TreeNode(root[i]) if root[i] is not None else None
            i += 1
            q.append(curr.left)
            if i<len(root):
                curr.right = TreeNode(root[i]) if root[i] is not None else None
                q.append(curr.right)
        i += 1
    return start

def print_tree(start):
    res = []
    q = deque([start])
    while any(q):
        curr = q.popleft()
        if curr:
            res.append(curr.val)
            q.extend([curr.left, curr.right])
        else:
            res.append(None)
    return res

null = None

root = [5,3,6,2,4,null,7]
key = 3
# Output: [5,4,6,2,null,null,7]

# root = [5,3,6,2,4,null,7]
# key = 0
# # Output: [5,3,6,2,4,null,7]

# root = []
# key = 0
# # Output: []

start = build_tree(root)
print(print_tree(start))

s = Solution()
res = s.deleteNode(start, key)
print(print_tree(res))
