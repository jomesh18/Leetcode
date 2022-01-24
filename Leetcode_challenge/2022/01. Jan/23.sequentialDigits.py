'''
1291. Sequential Digits
Medium

1454

95

Add to List

Share
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
Accepted
70,579
Submissions
116,099
'''
#iterative, O(n)
class Solution:
    def sequentialDigits(self, low: int, high: int) -> [int]:
        q = deque(range(1, 10))
        res = []
        while q:
            curr = q.popleft()
            if curr>=low and curr<=high:
                res.append(curr)
            last = curr % 10
            if last != 9:
                q.append(curr *10 + last + 1)
        return res

#O(nlogn)
class Solution:
    def sequentialDigits(self, low: int, high: int) -> [int]:
        self.res = []
        def dfs(num, i):
            if num>=low and num<= high:
                self.res.append(num)
            if num > high or i > 9:
                return
            dfs(num*10+i, i+1)

            for i in range(1, 10):
                dfs(0, i)
        return sorted(self.res)