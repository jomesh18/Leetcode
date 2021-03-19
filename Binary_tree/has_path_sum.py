'''
Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:

Input: root = [1,2], targetSum = 0
Output: false

 

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000


'''

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#iterative
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False

        q = deque([root])
        s = deque([root.val])
        while q:
        	curr = q.popleft()
        	curr_sum = s.popleft()
        	if curr:
        		if curr.left: 
        			s.append(curr_sum + curr.left.val)
        		else:
        			if curr_sum == targetSum: return True
        		if curr.right:
        			s.append(curr_sum + curr.right.val)
        		else:
        			if curr_sum == targetSum: return True
        	else:
        		if curr_sum == targetSum: return True
        return False

def create_tree(root):
	if not root:
		return
	start = TreeNode(root.pop(0))
	q = deque([start])
	while root:
		curr = q.popleft()
		if curr:
			l = root.pop(0)
			r = root.pop(0) if root else None
			curr.left = TreeNode(l) if l else None
			curr.right = TreeNode(r) if r else None
			q.extend([curr.left, curr.right])
	return start

def print_level_order(root):
	if not root: return None
	level = [root]
	ans = []
	while level:
		ans.append([i.val if i else None for i in level])
		level = [i for n in level if n for i in (n.left, n.right)]
	return ans

root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
# Output: true
start = create_tree(root)
print(print_level_order(start))
s = Solution()
print(s.hasPathSum(start, targetSum))
