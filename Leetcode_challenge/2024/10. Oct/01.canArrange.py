'''
1497. Check If Array Pairs Are Divisible by k
Medium

2430

149

Add to List

Share
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.

 

Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
 

Constraints:

arr.length == n
1 <= n <= 105
n is even.
-109 <= arr[i] <= 109
1 <= k <= 105
'''
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # if sum(arr) % k: return False
        rems = {}
        for e in arr:
            rems[e%k] = rems.get(e%k, 0) + 1
        i, j = 1, k-1
        while i <= j:
            if (i in rems) ^ (j in rems):
                return False
            if i in rems and ((i == j and rems[i] & 1) or (rems[i] != rems[j])):
                return False
            i += 1
            j -= 1
        return True