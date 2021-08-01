'''
Push Dominoes
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
        lst = list(dominoes)
        dist = [0] * len(dominoes)
        rDist = None
        for i, val in enumerate(lst):
            if val == 'R':
                rDist = 0
            elif val == 'L':
                rDist = None
            elif rDist != None:
                rDist += 1
                dist[i] = rDist
                lst[i] = 'R'
        lDist = None
        for i in range(len(lst) - 1, -1, -1):
            if dominoes[i] == 'L':
                lDist = 0
            elif dominoes[i] == 'R':
                lDist = None
            elif lDist != None:
                lDist += 1
                if lDist < dist[i] or lst[i] == '.':
                    lst[i] = 'L'
                elif lDist == dist[i]:
                    lst[i] = '.'
        return ''.join(lst)

dominoes = "RR.L"
# Output: "RR.L"

sol = Solution()
print(sol.pushDominoes(dominoes))
