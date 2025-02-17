'''

Code


Testcase
Testcase
Test Result
1718. Construct the Lexicographically Largest Valid Sequence
Solved
Medium
Topics
Companies
Hint
Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

 

Example 1:

Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
Example 2:

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]
 

Constraints:

1 <= n <= 20
'''
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        arr = [0]*(2*n-1)
        is_number_used = [False]*(n+1)

        def helper(arr, pos, is_number_used):
            if pos == 2*n-1:
                return arr

            if arr[pos] != 0:
                return helper(arr, pos+1, is_number_used)

            for num in range(n, 0, -1):
                if is_number_used[num]: continue

                arr[pos] = num
                is_number_used[num] = True

                if num == 1:
                    if helper(arr, pos+1, is_number_used):
                        return arr
                elif pos + num < 2*n-1 and not arr[pos+num]:
                    arr[pos+num] = num
                    if helper(arr, pos+1, is_number_used): return arr
                    arr[pos+num] = 0
                arr[pos] = 0
                is_number_used[num] = False

            return []

        return helper(arr, 0, is_number_used)
