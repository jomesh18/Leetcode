'''
729. My Calendar I
Medium

2680

73

Add to List

Share
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
 

Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.
Accepted
181,682
Submissions
323,527
'''
#binary search+insert
class MyCalendar:

    def __init__(self):
        self.calender = []
        self.start_to_end = {}

    def book(self, start: int, end: int) -> bool:
        if self.calender:
            ind = bisect.bisect_left(self.calender, start)
            if ind == len(self.calender):
                if start < self.start_to_end[self.calender[ind-1]]:
                    return False
            else:
                ind_start = self.calender[ind]
                ind_end = self.start_to_end[self.calender[ind]]
                if start == ind_start or end > ind_start: return False
                if ind != 0 and start < self.start_to_end[self.calender[ind-1]]: return False
            self.calender.insert(ind, start)
        else:
            self.calender.append(start)
        self.start_to_end[start] = end
        return True


#binary_tree
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.right = None
        self.left = None
        
    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif self.start >= node.end:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        return False
            
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)