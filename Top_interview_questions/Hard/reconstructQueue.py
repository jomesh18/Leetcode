'''
406. Queue Reconstruction by Height
Medium

6495

653

Add to List

Share
You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

 

Example 1:

Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
Example 2:

Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
 

Constraints:

1 <= people.length <= 2000
0 <= hi <= 106
0 <= ki < people.length
It is guaranteed that the queue can be reconstructed.
'''
# O(n*n)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0], x[1]))
        res = []
        for h, k in people:
            res.insert(k, [h, k])
        return res

# O(n*n)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = [0]*len(people)
        people.sort(key = lambda x:(x[0], -x[1]))
        # print(people)
        for h, i in people:
            empty_count = 0
            for j in range(len(res)):
                if res[j] == 0:
                    if empty_count == i:
                        break
                    empty_count += 1
            res[j] = [h, i]
        return res

# O(n*logn*logn)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        bit = [0]*(n+1)
        def update(i, delta):
            while i < (n+1):
                bit[i] += delta
                i += (i & -i)
                
        def getsum(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= (i & -i)
            return s
        
        for i in range(2, n+1):
            update(i, 1)
        people.sort(key = lambda x:(x[0], -x[1]))
        # print(people)
        res = [0]*n
        for i in range(n):
            l, r = 0, n
            while l < r:
                mid = (l+r)//2
                if getsum(mid + 1) < people[i][1]:
                    l = mid + 1
                else:
                    r = mid
            res[l] = people[i]
            update(l+1, -1)
        return res