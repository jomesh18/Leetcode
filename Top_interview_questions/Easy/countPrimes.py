'''
Count Primes

Solution
Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        i = 2
        while i*i < n:
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
            i += 1
        count = 0
        for i in range(n):
            count += 1 if primes[i] else 0
        return count

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0
        for i in range(2, int(n**.5)+1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
        return sum(primes)