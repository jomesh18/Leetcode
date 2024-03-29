'''
732. My Calendar III
Hard

1699

245

Add to List

Share
A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

You are given some events [start, end), after each given event, return an integer k representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class:

MyCalendarThree() Initializes the object.
int book(int start, int end) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.
 

Example 1:

Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]

Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1, The first event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(50, 60); // return 1, The second event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(10, 40); // return 2, The third event [10, 40) intersects the first event, and the maximum k-booking is a 2-booking.
myCalendarThree.book(5, 15); // return 3, The remaining events cause the maximum K-booking to be only a 3-booking.
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3
 

Constraints:

0 <= start < end <= 109
At most 400 calls will be made to book.
'''
from sortedcontainers import SortedList
class MyCalendarThree:

    def __init__(self):
        self.slist = SortedList()

    def book(self, start: int, end: int) -> int:
        self.slist.add((start, 1))
        self.slist.add((end, 0))
        kbook = 0
        ans = 0
        for e in self.slist:
            if not e[1]:
                kbook -= 1
            else:
                kbook += 1
            ans = max(ans, kbook)
        return ans

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)


from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.d[start] = self.d.get(start, 0) + 1
        self.d[end] = self.d.get(end, 0) - 1
        kbook = 0
        ans = 0
        for e in self.d.values():
            kbook += e
            ans = max(ans, kbook)
        return ans

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)


#using segment tree
from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.seg = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)
        
    def book(self, start, end):
        def update(s, e, l = 0, r = 10**9, ID = 0):
            if r <= s or e <= l: return 
            if s <= l and r <= e:
                self.seg[ID] += 1
                self.lazy[ID] += 1
            else:
                m = (l + r) // 2
                update(s, e, l, m, 2 * ID + 1)
                update(s, e, m, r, 2*ID+2)
                self.seg[ID] = self.lazy[ID] + max(self.seg[2*ID+1], self.seg[2*ID+2])
        update(start, end)
        return self.seg[0]

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)