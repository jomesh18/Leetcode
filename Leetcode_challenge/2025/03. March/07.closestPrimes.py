'''
2523. Closest Prime Numbers in Range
Solved
Medium
Topics
Companies
Hint
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

Constraints:

1 <= left <= right <= 106
'''
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True]*(right+1)
        primes[0] = False
        primes[1] = False
        p = 2
        while p*p <= right:
            if primes[p]:
                for i in range(p*p, right+1, p):
                    primes[i] = False
            p += 1

        primes_between = []
        for i in range(left, right+1):
            if primes[i]:
                primes_between.append(i)
        
        if len(primes_between) < 2: return [-1, -1]
        diff = right-left+1
        ans = [left, right]
        for i in range(1, len(primes_between)):
            if primes_between[i] - primes_between[i-1] < diff:
                diff = primes_between[i] - primes_between[i-1]
                ans = [primes_between[i-1], primes_between[i]]
        return ans
        