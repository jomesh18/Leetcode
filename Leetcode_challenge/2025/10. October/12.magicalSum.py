'''
3539. Find Sum of Array Product of Magical Sequences
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given two integers, m and k, and an integer array nums.

A sequence of integers seq is called magical if:
seq has a size of m.
0 <= seq[i] < nums.length
The binary representation of 2seq[0] + 2seq[1] + ... + 2seq[m - 1] has k set bits.
The array product of this sequence is defined as prod(seq) = (nums[seq[0]] * nums[seq[1]] * ... * nums[seq[m - 1]]).

Return the sum of the array products for all valid magical sequences.

Since the answer may be large, return it modulo 109 + 7.

A set bit refers to a bit in the binary representation of a number that has a value of 1.

 

Example 1:

Input: m = 5, k = 5, nums = [1,10,100,10000,1000000]

Output: 991600007

Explanation:

All permutations of [0, 1, 2, 3, 4] are magical sequences, each with an array product of 1013.

Example 2:

Input: m = 2, k = 2, nums = [5,4,3,2,1]

Output: 170

Explanation:

The magical sequences are [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 4], [4, 0], [4, 1], [4, 2], and [4, 3].

Example 3:

Input: m = 1, k = 1, nums = [28]

Output: 28

Explanation:

The only magical sequence is [0].

 

Constraints:

1 <= k <= m <= 30
1 <= nums.length <= 50
1 <= nums[i] <= 108
'''
class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        def binary_exp(a, b):
            if b == 0:
                return 1
            half = binary_exp(a, b//2)
            ans = (half * half) % MOD
            if b & 1:
                ans = (ans * a) % MOD
            return ans

        def nCr(n, r):
            return (((fact[n]*inv_fact[r]) % MOD) * inv_fact[n-r]) % MOD

        fact = [1]*(m+1)
        for i in range(2, m+1):
            fact[i] = (fact[i-1] * i) % MOD
        inv_fact = [1]*(m+1)
        for i in range(m+1):
            inv_fact[i] = binary_exp(fact[i], MOD-2)

        memo = {}
        def solve(binary_sum, i, m, k):
            if m == 0 and binary_sum.bit_count() == k:
                return 1
            if m == 0 or i >= n:
                return 0
            key = (binary_sum, i, m, k)
            if key in memo: return memo[key]
            total_sum = solve(binary_sum>>1, i+1, m, k - (binary_sum & 1))
            for freq in range(1, m+1):
                new_binary_sum = binary_sum + freq
                prod = solve(new_binary_sum>>1, i+1, m-freq, k - (new_binary_sum & 1))
                prod = (binary_exp(nums[i], freq) * prod) % MOD
                prod = (prod * nCr(m, freq)) % MOD
                total_sum = (prod + total_sum) % MOD

            memo[key] = total_sum
            return total_sum

        return solve(0, 0, m, k)
