'''
823. Binary Trees With Factors
Medium

1286

134

Add to List

Share
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 

Constraints:

1 <= arr.length <= 1000
2 <= arr[i] <= 109
All the values of arr are unique.
Accepted
48,685
Submissions
105,462
'''
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        mod = 10**9+7
        n = len(arr)
        index = {x: i for i, x in enumerate(arr)}
        dp = [1]*n
        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0: #arr[j] will be left child
                    right = x//arr[j]
                    if right in index:
                        dp[i] += dp[j]*dp[index[right]]
                        dp[i] %= mod
        return sum(dp)%mod