'''
1291. Sequential Digits
Medium

2087

124

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
'''
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        str_low = str(low)
        str_high = str(high)
        
        ans = []
        for l in range(len(str_low), len(str_high)+1):
            for start in range(1, 10):
                if start + l > 10: break
                curr = 0
                for num in range(start, start + l):
                    curr = curr * 10 + num
                    if curr >= low and curr <= high and (curr//int('1'+'0'*(l-1))):
                        ans.append(curr)
                    if curr > high:
                        break
        return ans
