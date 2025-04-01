'''
2818. Apply Operations to Maximize Score
Solved
Hard
Topics
Companies
Hint
You are given an array nums of n positive integers and an integer k.

Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:

Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the one with the smallest index.
Multiply your score by x.
Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.

The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.

Return the maximum possible score after applying at most k operations.

Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [8,3,9,3,8], k = 2
Output: 81
Explanation: To get a score of 81, we can apply the following operations:
- Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
It can be proven that 81 is the highest score one can obtain.
Example 2:

Input: nums = [19,12,14,6,10,18], k = 3
Output: 4788
Explanation: To get a score of 4788, we can apply the following operations: 
- Choose subarray nums[0, ..., 0]. nums[0] is the only element in this subarray. Hence, we multiply the score by nums[0]. The score becomes 1 * 19 = 19.
- Choose subarray nums[5, ..., 5]. nums[5] is the only element in this subarray. Hence, we multiply the score by nums[5]. The score becomes 19 * 18 = 342.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 2, but nums[2] has the smaller index. Hence, we multipy the score by nums[2]. The score becomes 342 * 14 = 4788.
It can be proven that 4788 is the highest score one can obtain.
 

Constraints:

1 <= nums.length == n <= 105
1 <= nums[i] <= 105
1 <= k <= min(n * (n + 1) / 2, 109)
'''
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        n = len(nums)
        upper_limit = max(nums)+1
        prime_cands = [True for _ in range(upper_limit)]
        prime_cands[0] = False
        prime_cands[1] = False
        for i in range(2, int(upper_limit**.5)+1):
            if prime_cands[i]:
                for j in range(i*i, upper_limit, i):
                    prime_cands[j] = False

        primes = [i for i in range(upper_limit) if prime_cands[i]]

        def find_prime_score(num, primes):
            prime_score = 0
            for prime in primes:
                if prime * prime > num: break
                if num % prime: continue
                prime_score += 1
                while num % prime == 0:
                    num //= prime
            if num > 1: prime_score += 1
            return prime_score

        prime_scores = [find_prime_score(num, primes) for num in nums]
        # print('prime_scores', prime_scores)
        prime_score_from_right = [-1]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            prime_score_from_right[i] = stack[-1] if stack else n
            stack.append(i)
        # print('prime_score_from_right', prime_score_from_right)
        stack = []
        prime_score_from_left = [-1]*n
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            prime_score_from_left[i] = stack[-1] if stack else -1
            stack.append(i)
        # print('prime_score_from_left', prime_score_from_left)
        def _power(base, exponent):
            res = 1
            while exponent > 0:
                if exponent & 1:
                    res = (res*base) % MOD
                base = (base*base) % MOD
                exponent //= 2
            return res
            
        scores = [-1]*n
        for i in range(n):
            scores[i] = (nums[i], (prime_score_from_right[i] - i) * (i - prime_score_from_left[i]))
        # print('scores', scores)
        scores.sort(reverse=True)
        # print('sorted_scores', scores)
        max_score = 1
        rem = k
        i = 0
        while rem > 0:
            qty = min(scores[i][1], rem)
            exp = _power(scores[i][0], qty)
            max_score = (max_score * exp)% MOD
            rem -= qty
            i += 1
        return max_score
