'''
  Guess Number Higher or Lower

Solution
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
Example 4:

Input: n = 2, pick = 2
Output: 2
 

Constraints:

1 <= n <= 231 - 1
1 <= pick <= n
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution2:
    def guessNumber(self, n: int) -> int:
        def guess(num):
            # print(num, pick)
            if pick > num:
                return 1
            elif pick < num:
                return -1
            else:
                return 0

        l, r = 1, n+1
        while l < r:
            my_guess = l + ((r-l)>>1)
            res = guess(my_guess)
            print(l, r, my_guess)
            if res == 0:
                return my_guess
            elif res == -1:
                r = my_guess
            else:
                l = my_guess + 1

#from leetcode
class Solution:
    def guessNumber(self, n):
        def guess(num):
            # print(num, pick)
            if pick > num:
                return 1
            elif pick < num:
                return -1
            else:
                return 0
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            print(lo, hi, mid)
            if guess(mid) == 1:
                lo = mid + 1
            else:
                hi = mid
        return lo

n = 10
pick = 10
# Output: 6
# n = 1
# pick = 1
# # Output: 1
# n = 2
# pick = 1
# # Output: 1
# n = 2
# pick = 2
# # Output: 2
s = Solution()
print(s.guessNumber(n))
s2 = Solution2()
print(s2.guessNumber(n))