'''
846. Hand of Straights
Medium

2756

201

Add to List

Share
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

 

Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
 

Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
'''
# O(nlogn)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        count = Counter(hand)
        for key in sorted(count.keys()):
            if count[key]:
                val = count[key]
                for delta in range(1, groupSize):
                    if count[key+delta] < val:
                        return False
                    count[key+delta] -= val

        return True


# O(n) time
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        for card in count.keys():
            start = card
            while count[start-1]:
                start -= 1
            while start <= card:
                if count[start]:
                    val = count[start]
                    count[start] -= val
                    for curr in range(start+1, start+groupSize):
                        count[curr] -= val
                        if count[curr] < 0: return False
                start += 1
        return True
