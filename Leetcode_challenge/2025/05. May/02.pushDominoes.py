'''
838. Push Dominoes
Solved
Medium
Topics
premium lock icon
Companies
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

 

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
 

Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.
'''
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        left, right = [0]*n, [0]*n
        f = 0
        for i in range(n):
            if dominoes[i] == 'R':
                f = n
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f-1, 0)
            left[i] = f

        f = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                f = -n
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = min(f+1, 0)
            right[i] = f

        res = ['']*n
        for i in range(n):
            val = left[i] + right[i]
            if val > 0:
                res[i] = 'R'
            elif val < 0:
                res[i] = 'L'
            else:
                res[i] = '.'
        return ''.join(res)
