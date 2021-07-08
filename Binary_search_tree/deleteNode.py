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

#my try
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        dummy = TreeNode(float("-inf"), None, root)
        def find_pos(node, key):
            curr = node
            pos = (node, 1)
            while curr:
                if key > curr.val:
                    pos = (curr, 1)
                    curr = curr.right
                elif key < curr.val:
                    pos = (curr, 0)
                    curr = curr.left
                else:
                    break
            return (curr, pos)

        def inorderSuccessor(curr):
            node = root
            succ = None
            while node:
                if node.val <= curr.val:
                    node = node.right
                else:
                    succ = node
                    node = node.left
            return succ

        key_node, p = find_pos(dummy, key)
        node_above_key_node, key_node_is_right_child = p[0], p[1]
        if not key_node: return dummy.right
        if key_node.left is None and key_node.right is None: #delete a leaf node
            if key_node_is_right_child:
                node_above_key_node.right = None
            else:
                node_above_key_node.left = None
            return dummy.right
        elif key_node.right is None: # delete node with no right subtree
            if key_node_is_right_child:
                node_above_key_node.right = key_node.left
            else:
                node_above_key_node.left = key_node.left
            return dummy.right

        succ = inorderSuccessor(key_node)
        parent_successor = None
        t1, t2 = find_pos(dummy, succ.val)
        parent_successor, succ_right_child_of_parent = t2
        if succ_right_child_of_parent:
            parent_successor.right = None
        else:
            parent_successor.left = None
        succ.left = key_node.left
        curr = succ
        prev = succ
        while curr:
            prev = curr
            curr = curr.right
        prev.right = key_node.right
        if key_node_is_right_child:
            node_above_key_node.right = succ
        else:
            node_above_key_node.left = succ

        return dummy.right

def build_tree(root):
    if not root: return root
    start = TreeNode(root[0])
    q = deque([start])
    i = 1
    while i<len(root):
        # print(i, root[i:], q)
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
# # Output: [5,4,6,2,null,null,7]

root = [5,3,6,2,4,null,7]
key = 0
# # # # # # # Output: [5,3,6,2,4,null,7]

root = []
key = 0
# # # # # # # Output: []

root = [0]
key = 0
# # # # Output: []

root = [50,30,70,null,40,60,80]
key = 50
# # # Output: [60, 30, 70, None, 40, None, 80]

root = [5,3,6,2,4,null,7]
key = 5
# # # # Output : [6, 3, 7, 2, 4]

root = [2,1]
key = 2
# # # Output = [1]

root = [2,1]
key = 1
# # Output = [2]

root = [50,30,70,null,40,60,80]+[None]*2+[55,57,75,85]+[None]*5+[76]+[None]*3+[77]
key = 70

start = build_tree(root)
print(print_tree(start))

s = Solution()
res = s.deleteNode(start, key)
print(print_tree(res))
