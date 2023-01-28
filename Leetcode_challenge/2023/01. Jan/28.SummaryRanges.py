'''
352. Data Stream as Disjoint Intervals
Hard

1043

235

Add to List

Share
Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

SummaryRanges() Initializes the object with an empty stream.
void addNum(int value) Adds the integer value to the stream.
int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
 

Example 1:

Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
 

Constraints:

0 <= value <= 104
At most 3 * 104 calls will be made to addNum and getIntervals.
 

Follow up: What if there are lots of merges and the number of disjoint intervals is small compared to the size of the data stream?
'''
class SummaryRanges:

    def __init__(self):
        self.ints = []

    def addNum(self, value: int) -> None:
        pos = self.b_right(self.ints, value)
        if pos == 0:
            if self.ints and self.ints[0][0] - 1 == value:
                self.ints[pos][0] = value
            else:
                self.ints.insert(pos, [value, value])
        elif pos == len(self.ints):
            if value <= self.ints[-1][1]:
                return
            elif value == self.ints[-1][1] + 1:
                self.ints[-1][1] = value
            else:
                self.ints.append([value, value])
        else:
            if self.ints[pos-1][1] >= value or self.ints[pos][0] == value:
                return
            elif self.ints[pos-1][1] == value-1 and self.ints[pos][0] == value+1:
                self.ints[pos] = [self.ints[pos-1][0], self.ints[pos][1]]
                self.ints.pop(pos-1)
            elif self.ints[pos][0] - 1 == value:
                self.ints[pos][0] = value
            elif self.ints[pos-1][1] + 1 == value:
                self.ints[pos-1][1] = value
            else:
                self.ints.insert(pos, [value, value])
    
    def b_right(self, l, value):
        lo, hi = 0, len(l)
        while lo < hi:
            mid = (lo + hi)//2
            if value < l[mid][0]:
                hi = mid
            else:
                lo = mid + 1
        return lo
        
    def getIntervals(self) -> List[List[int]]:
        # print(self.ints)
        return self.ints


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()