'''
1010. Pairs of Songs With Total Durations Divisible by 60
Medium

2729

105

Add to List

Share
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500
Accepted
169,071
Submissions
313,988
'''
class Solution:
    def numPairsDivisibleBy60(self, time: [int]) -> int:
        modulo_60 = [0 for _ in range(60)]
        for t in time:
            modulo_60[t%60] += 1
        beg, end = 1, 59
        ans = 0
        # print(modulo_60)
        while beg < end:
            ans += modulo_60[beg] * modulo_60[end]
            beg += 1
            end -= 1
        mid = modulo_60[beg]
        s = modulo_60[0]
        return ans+ (mid*(mid-1)//2) + (s*(s-1)//2)


class Solution:
    def numPairsDivisibleBy60(self, time: [int]) -> int:
        res = 0
        d = [0 for _ in range(60)]
        for t in time:
            res += d[(60-t%60)%60]
            d[t%60] += 1
        return res
