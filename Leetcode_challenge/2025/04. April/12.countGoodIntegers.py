'''
3272. Find the Count of Good Integers
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given two positive integers n and k.

An integer x is called k-palindromic if:

x is a palindrome.
x is divisible by k.
An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.

Return the count of good integers containing n digits.

Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.

 

Example 1:

Input: n = 3, k = 5

Output: 27

Explanation:

Some of the good integers are:

551 because it can be rearranged to form 515.
525 because it is already k-palindromic.
Example 2:

Input: n = 1, k = 4

Output: 2

Explanation:

The two good integers are 4 and 8.

Example 3:

Input: n = 5, k = 6

Output: 2468

 

Constraints:

1 <= n <= 10
1 <= k <= 9
'''
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
        def find_k_palins(k_palins, n):
            odd = False
            if n & 1:
                odd = True
            half = (n+1)>>1
            for i in range(10**(half-1), 10**half):
                str_i = str(i)
                if odd:
                    palin = str_i + str_i[:-1][::-1]
                else:
                    palin = str_i + str_i[::-1]
                if int(palin) % k == 0:
                    k_palins.add(''.join(sorted(palin)))
        
        k_palins = set()
        find_k_palins(k_palins, n)
        fact_n_1 = factorial(n-1)
        ans = 0
        for p in k_palins:
            count = Counter(p)
            curr = fact_n_1
            non_zero = 0
            f = 1
            for key, freq in count.items():
                if key != '0':
                    non_zero += freq
                f *= factorial(freq)
            curr *= non_zero
            curr //= f
            ans += curr
        
        return ans
