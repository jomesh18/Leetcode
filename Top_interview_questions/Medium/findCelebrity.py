'''
https://www.lintcode.com/problem/645/
645 · Find the Celebrity
Algorithms
Medium
Accepted Rate
48%
Description
Solution19
Notes99+
Discuss3
Leaderboard
Record
Description
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

Example
Example1

Input:
2 // next n * (n - 1) lines 
0 knows 1
1 does not know 0
Output: 1
Explanation:
Everyone knows 1,and 1 knows no one.
Example2

Input:
3 // next n * (n - 1) lines 
0 does not know 1
0 does not know 2
1 knows 0
1 does not know 2
2 knows 0
2 knows 1
Output: 0
Explanation:
Everyone knows 0,and 0 knows no one.
0 does not know 1,and 1 knows 0.
2 knows everyone,but 1 does not know 2.
Tags
'''
"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        candidates = set(i for i in range(n))
        to_visit = set(i for i in range(n))
        def helper(i):
            is_celebrity = True
            for k in range(n):
                if k != i:
                    if Celebrity.knows(i, k):
                        if k in to_visit:
                            to_visit.remove(k)
                            if helper(k) is not None: return k
                        is_celebrity = False
                        break
                    else:
                        if k in candidates: candidates.remove(k)
            if is_celebrity: return i
            if i in candidates: candidates.remove(i)
            return None

        for i in range(n):
            if i in candidates:
                if i in to_visit:
                    to_visit.remove(i)
                helper(i)
        for k in candidates:
            is_celebrity = True
            for i in range(n):
                if i != k and not Celebrity.knows(i, k):
                    is_celebrity = False
                    break
            if is_celebrity: return k
        return -1



class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        celeb = 0
        
        for i in range(1, n):
            if Celebrity.knows(celeb, i):
                celeb = i
        
        # Check if the final candicate is the celebrity
        for i in range(n):
            if celeb != i and Celebrity.knows(celeb, i):
                return -1
            if celeb != i and not Celebrity.knows(i, celeb):
                return -1
        
        return celeb


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        celeb = 0
        for i in range(1, n):
            if Celebrity.knows(celeb, i):
                celeb = i

        for i in range(n):
            if i != celeb:
                if not Celebrity.knows(i, celeb) or Celebrity.knows(celeb, i):
                    return -1
        return celeb