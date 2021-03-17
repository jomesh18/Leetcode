'''
  Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

 
Follow up: Could you solve it both recursively and iteratively?
'''

# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
    	left_level = root.left
    	right_level = root.right
    	
    	if left_level != right_level:
    		return False
    	left_level = [l for n in left_level for l in (n.left, n.right)]
    	right_level = [l for n in right_level for l in (n.left, n.right)]


        
def construct_tree(root):
	start = TreeNode(root[0])
	q = deque([start])
	i = 1
	while i < len(root):
		curr = q.popleft()
		if root[i] is not None:
			curr.left = TreeNode(root[i])
			q.append(curr.left)
		i += 1
		if root[i] is not None:
			curr.right = TreeNode(root[i])
			q.append(curr.right)
		i += 1
	return start

def print_level_order(root):
	level = [root]
	ans = []
	while root and level:
		ans.append([n.val for n in level])
		level = [n_l for n in level for n_l in (n.left, n.right) if n_l]
	return ans

root = [1,2,2,3,4,4,3]
# Output: true
start = construct_tree(root)
print(print_level_order(start))
s = Solution()
print(s.isSymmetric(start))
