'''
564. Find the Closest Palindrome
Hard

994

1575

Add to List

Share
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 

Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].
'''
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        def find_palin(left, even):
            res = left
            if not even: 
                left //= 10
            while left:
                res = res * 10 + left % 10
                left //= 10
            return res
        candidates = []
        is_even = False if l & 1 else True
        mid = l//2 if l & 1 else l//2-1
        candidates.append(find_palin(int(n[:mid+1]), is_even))
        candidates.append(find_palin(int(n[:mid+1])+1, is_even))
        candidates.append(find_palin(int(n[:mid+1])-1, is_even))
        candidates.append(int('1'+'0'*(l-1))-1)
        candidates.append(int('1'+'0'*(l-1)+'1'))
        
        diff = float('inf')
        curr_res = 0
        int_n = int(n)
        for cand in candidates:
            if cand == int_n:
                continue
            curr_diff = abs(cand-int_n)
            if curr_diff < diff:
                diff = curr_diff
                curr_res = cand
            elif curr_diff == diff:
                curr_res = min(cand, curr_res)
        return str(curr_res)