'''
605. Can Place Flowers
Easy

2297

580

Add to List

Share
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''
#accepted linear scan
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for curr in range(len(flowerbed)):
            if curr-1 >=0 and curr+1 < len(flowerbed):
                if flowerbed[curr-1] == 0 and flowerbed[curr] == 0 and flowerbed[curr+1] == 0:
                    flowerbed[curr] = 1
                    n -= 1
            else:
                if curr == 0:
                    if curr+1 < len(flowerbed):
                        if flowerbed[curr+1] == 0:
                            if flowerbed[curr] == 0:
                                flowerbed[curr] = 1
                                n -= 1
                    else:
                        if flowerbed[curr] == 0:
                            flowerbed[curr] = 1
                            n -= 1
                else:
                    if curr == len(flowerbed)-1:
                        if flowerbed[curr-1] == 0:
                            if flowerbed[curr] == 0:
                                flowerbed[curr] = 1
                                n -= 1
        return n <= 0

#elegent linear scan from leetcode solution
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n <= 0:
                    return True
        return False
