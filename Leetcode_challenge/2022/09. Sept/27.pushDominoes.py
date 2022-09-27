'''
838. Push Dominoes
Medium

2177

143

Add to List

Share
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
        visited = set()
        r, l = set(), set()
        for i, c in enumerate(dominoes):
            if c == 'R':
                r.add(i)
                visited.add(i)
            elif c == 'L':
                l.add(i)
                visited.add(i)
        tr, tl = set(), set()
        for i in r:
            if i-1 in r:
                tr.add(i-1)
        for i in l:
            if i+1 in l:
                tl.add(i+1)
        for i in tr:
            r.remove(i)
        for i in tl:
            l.remove(i)
        res = list(dominoes)
        # print(res)
        # print(r, l)
        while len(visited) < n and (r or l):
            nr, nl = set(), set()
            for i in r:
                if i+1 not in visited and i+1 < n:
                    nr.add(i+1)
            for i in l:
                if i-1 >= 0 and i-1 not in visited:
                    if i-1 in nr:
                        nr.remove(i-1)
                        visited.add(i-1)
                    else:
                        nl.add(i-1)
            for i in nr:
                visited.add(i)
                res[i] = 'R'
            for i in nl:
                visited.add(i)
                res[i] = 'L'
            r, l = nr, nl
            # print(visited)
            # print(r, l)
        ans = ''.join(res)
        # print(ans)
        return ans


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        symbols = [(-1, 'L')] + [(i, x) for i, x in enumerate(dominoes) if x != '.'] + [(len(dominoes), 'R')]
        ans = list(dominoes)
        
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            elif x > y:
                for k in range(i+1, j):
                    if k-i < j-k:
                        ans[k] = x
                    elif k-i > j-k:
                        ans[k] = y
                    else:
                        ans[k] = '.'
        return ''.join(ans)