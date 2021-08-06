'''
771. Encode N-ary Tree to Binary Tree
Difficulty: Hard

Topics: Tree

Similar Questions:

Serialize and Deserialize N-ary Tree
Problem:
Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original N-nary tree structure.

For example, you may encode the following 3-ary tree to a binary tree in this way:

 



 

Note that the above is just an example which might or might not work. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Note:

N is in the range of  [1, 1000]
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
'''
from collections import deque
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: binary tree
    @return: N-ary tree
    """
    # def decode(self, root):
    #     # write your code here
    #     q = deque([(root, UndirectedGraphNode(root.val))])
    #     n_start = q[0][1]
    #     while q:
    #         b_curr, n_curr = q.popleft()
    #         if b_curr.left:
    #             b_curr = b_curr.left
    #             while b_curr:
    #                 n_curr.neighbors.append(UndirectedGraphNode(b_curr.val))
    #                 q.append([b_curr, n_curr.neighbors[-1]])
    #                 b_curr = b_curr.right
    #     return n_start

    """
    @param root: N-ary tree
    @return: binary tree
    """
    # def encode(self, root):
    #     # write your code here
    #     if not root: return []
    #     q = deque([(root, TreeNode(root.label))])
    #     bin_start = q[-1][1]
    #     while q:
    #         # print([(u[0].label, u[1].val) for u in q])
    #         curr, bin_curr = q.popleft()
    #         # if not bin_curr: bin_curr = TreeNode(curr.label)
    #         if curr.neighbors:
    #             bin_curr.left = TreeNode(curr.neighbors[0].label)
    #             q.append((curr.neighbors[0], bin_curr.left))
    #             bin_curr = bin_curr.left
    #             for n in curr.neighbors[1:]:
    #                 bin_curr.right = TreeNode(n.label)
    #                 q.append((n, bin_curr.right))
    #                 bin_curr = bin_curr.right
    #     return bin_start

    # def decode(self, root):
    #     if not root:
    #         return None
    
    #     res = UndirectedGraphNode(root.val)
    #     cur = root.left
        
    #     while cur:
    #         res.neighbors.append(self.decode(cur))
    #         cur = cur.right
       
    #     return res

    """
    @param root: N-ary tree
    @return: binary tree
    """
    # def encode(self, root):
    #     if not root:
    #         return None
    
    #     res = TreeNode(root.label)
        
    #     if root.neighbors: 
    #         res.left = self.encode(root.neighbors[0])
            
    #     cur = res.left
        
    #     for i in range(1, len(root.neighbors)):
    #         cur.right = self.encode(root.neighbors[i])
    #         cur = cur.right
        
    #     return res
#my try
    def encode(self, root):
        if not root: return None
        res = TreeNode(root.label)
        if root.neighbors:
            res.left = self.encode(root.neighbors[0])
            curr = res.left
            for i in range(1, len(root.neighbors)):
                curr.right = self.encode(root.neighbors[i])
                curr = curr.right
        return res
#my try
    def decode(self, root):
        if not root: return None
        res = UndirectedGraphNode(root.val)
        curr = root.left
        while curr:
            res.neighbors.append(self.decode(curr))
            curr = curr.right
        return res

def build_nary_tree(root):
    if not root: return []
    start = UndirectedGraphNode(root[0])
    i = 2
    q = deque([start])
    while i < len(root):
        curr = q.popleft()
        while i<len(root) and root[i] is not None:
            curr.neighbors.append(UndirectedGraphNode(root[i]))
            i += 1
        q.extend(curr.neighbors)
        i += 1
    return start

def print_nary(start):
    if not start: return []
    q = deque([start])
    res = [start.label, None]
    while any(q):
        curr = q.popleft()
        if curr and curr.neighbors:
            res.extend([n.label for n in curr.neighbors])
            q.extend(curr.neighbors)
        res.append(None)
    return res

def print_binary(start):
    res = []
    if not start: return res
    q = deque([start])
    while any(q):
        curr = q.popleft()
        if curr:
            res.append(curr.val)
            q.extend([curr.left, curr.right])
        else:
            res.append(None)
    return res

root = [1, None, 2, 3, 4, None, 5, None, 6]

root = [1, None, 3, 2, 4, None, 5, 6]
# {1,2,3,4#2#3,5,6#4#5#6}

start = build_nary_tree(root)

print(print_nary(start))
sol = Solution()
b_tree = sol.encode(start)
print(print_binary(b_tree))
n_tree = sol.decode(b_tree)
print(print_nary(n_tree))
