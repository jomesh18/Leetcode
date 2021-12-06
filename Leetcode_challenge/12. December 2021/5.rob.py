'''
337. House Robber III
Medium

5435

86

Add to List

Share
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:


Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:


Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 104
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#recursive, brute force
class Solution:
    def rob(self, root) -> int:
        def helper(root, canRob):
            if not root: return 0
            robbing_current = root.val + helper(root.left, False) + helper(root.right, False) if canRob else -1
            not_robbing_current = helper(root.left, True) + helper(root.right, True)
            return max(robbing_current, not_robbing_current)
        helper(root, True)

#recursive, brute force
class Solution:
    def rob(self, root) -> int:
        if not root: return 0
        robbing_current, not_robbing_current = root.val, self.rob(root.left) + self.rob(root.right)
        if root.left: robbing_current += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right: robbing_current += self.rob(root.right.left) + self.rob(root.right.right)
        return max(robbing_current, not_robbing_current)

#first with memo
class Solution:
    def rob(self, root) -> int:
        d = {}
        def helper(root, canRob):
            if not root: return 0
            if (root, canRob) in d: return d[(root, canRob)]
            robbing_current = root.val + helper(root.left, False) + helper(root.right, False) if canRob else -1
            not_robbing_current = helper(root.left, True) + helper(root.right, True)
            d[(root, canRob)] = max(robbing_current, not_robbing_current)
            return d[(root, canRob)]
        return helper(root, True)

#second with memo
class Solution:
    def __init__(self):
        self.d = {}
    def rob(self, root) -> int:
        if not root: return 0
        if root in self.d: return self.d[root]
        robbing_current, not_robbing_current = root.val, self.rob(root.left) + self.rob(root.right)
        if root.left: robbing_current += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right: robbing_current += self.rob(root.right.left) + self.rob(root.right.right)
        self.d[root] = max(robbing_current, not_robbing_current)
        return self.d[root]


#from leetcode, space optimized dp
'''
Step III -- Think one step back

In step I, we defined our problem as rob(root), which will yield the maximum amount of money that can be robbed of the binary tree rooted at root. This leads to the DP problem summarized in step II.

Now let's take one step back and ask why we have overlapping subproblems. If you trace all the way back to the beginning, you'll find the answer lies in the way how we have defined rob(root). As I mentioned, for each tree root, there are two scenarios: it is robbed or is not. rob(root) does not distinguish between these two cases, so "information is lost as the recursion goes deeper and deeper", which results in repeated subproblems.

If we were able to maintain the information about the two scenarios for each tree root, let's see how it plays out. Redefine rob(root) as a new function which will return an array of two elements, the first element of which denotes the maximum amount of money that can be robbed if root is not robbed, while the second element signifies the maximum amount of money robbed if it is robbed.

Let's relate rob(root) to rob(root.left) and rob(root.right)..., etc. For the 1st element of rob(root), we only need to sum up the larger elements of rob(root.left) and rob(root.right), respectively, since root is not robbed and we are free to rob its left and right subtrees. For the 2nd element of rob(root), however, we only need to add up the 1st elements of rob(root.left) and rob(root.right), respectively, plus the value robbed from root itself, since in this case it's guaranteed that we cannot rob the nodes of root.left and root.right.

As you can see, by keeping track of the information of both scenarios, we decoupled the subproblems and the solution essentially boiled down to a greedy one. Here is the program:
'''
class Solution:
    def rob(self, root) -> int:
        def dfs(root):
            if not root: return (0, 0)
            L, R = dfs(root.left), dfs(root.right)
            return (max(L) + max(R), root.val + L[0] + R[0])
        return max(dfs(root))


null = None

root = [4, 5, 6, 11, 20]

root = [4, 1, 2, 3]

root = [2,1,3,null,4]

sol = Solution()
print(sol.rob(root))
