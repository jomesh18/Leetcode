'''
My Calendar I
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
 

Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
 

   Show Hint #1  

'''

class MyCalendar:

    def __init__(self):
        self.event = []

    def book(self, start: int, end: int) -> bool:
        for b, e in self.event:
                # print(self.event)
                if not (start<end<=b or e<=start<end):
                        return False
        self.event.append((start,end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

obj = MyCalendar()
null = None
true = True
false = False

Input = ["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
para = [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
Output = [null,true,true,false,false,true,false,true,true,true,false]
out = [None]
for fn, par in zip(Input, para):
        if fn == "book":
                out.append(obj.book(par[0], par[1]))
        elif fn == "MyCalendar":
                pass
print(Output)
print(out)                
print(Output == out)
