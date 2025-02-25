'''
1524. Number of Sub-arrays With Odd Sum
Solved
Medium
Topics
Companies
Hint
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 100
'''
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        odd_odds = 0
        even_odds = 0
        ans = 0

        curr_odds = 0
        last_odd_i = -1
        for i, num in enumerate(arr):
            if num & 1:
                curr_odds += 1
                if curr_odds & 1:
                    odd_odds = (odd_odds + i-last_odd_i) % MOD
                    ans = (ans + odd_odds) % MOD
                else:
                    even_odds = (even_odds + i-last_odd_i) % MOD
                    ans = (ans + even_odds) % MOD
                last_odd_i = i
            else:
                if not curr_odds:
                    continue
                elif curr_odds & 1:
                    ans = (ans + odd_odds) % MOD
                else:
                    ans = (ans + even_odds) % MOD
            # print(i, ans)
        return ans