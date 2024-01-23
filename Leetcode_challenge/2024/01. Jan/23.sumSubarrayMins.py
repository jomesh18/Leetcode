'''
907. Sum of Subarray Minimums
Medium

7751

583

Add to List

Share
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
'''
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack = [0]
        ans_arr = [0]*len(arr)
        ans_arr[0] = arr[0]
        MOD = 10 ** 9 + 7
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                ans_arr[i] = (ans_arr[stack[-1]] + ((i-stack[-1])*arr[i]) % MOD) % MOD
            else:
                ans_arr[i] = (arr[i]*(i+1)) % MOD
            stack.append(i)
        ans = 0
        for a in ans_arr:
            ans = (ans + a) % MOD
        return ans
        