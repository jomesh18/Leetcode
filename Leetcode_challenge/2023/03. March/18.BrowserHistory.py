'''
1472. Design Browser History
Medium

2781

170

Add to List

Share
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
 

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
 

Constraints:

1 <= homepage.length <= 20
1 <= url.length <= 20
1 <= steps <= 100
homepage and url consist of  '.' or lower case English letters.
At most 5000 calls will be made to visit, back, and forward.
'''
class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.pos += 1
        self.arr = self.arr[:self.pos]
        self.arr.append(url)

    def back(self, steps: int) -> str:
        self.pos = max(self.pos-steps, 0)
        return self.arr[self.pos]

    def forward(self, steps: int) -> str:
        self.pos = min(self.pos+steps, len(self.arr)-1)
        return self.arr[self.pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


# two stacks
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.future = []
        self.curr = homepage

    def visit(self, url: str) -> None:
        self.history.append(self.curr)
        self.curr = url
        self.future = []

    def back(self, steps: int) -> str:
        while steps and self.history:
            self.future.append(self.curr)
            self.curr = self.history.pop()
            steps -= 1
        return self.curr

    def forward(self, steps: int) -> str:
        while steps and self.future:
            self.history.append(self.curr)
            self.curr = self.future.pop()
            steps -= 1
        return self.curr


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


# using double linked list, visit O(l), back and forward O(min(n, m)) where l is the max length of the string and n is the total calls and m is the steps
# space O(l*n)
class DLLNode:
    def __init__(self, url):
        self.data = url
        self.next, self.prev = None, None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = DLLNode(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        self.curr.next = DLLNode(url)
        self.curr.next.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while steps and self.curr.prev:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.data

    def forward(self, steps: int) -> str:
        while steps and self.curr.next:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.data


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


# dynamic array
# O(1) time
class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.curr = 0
        self.last = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if len(self.urls) > self.curr:
            self.urls[self.curr] = url
        else:
            self.urls.append(url)
        self.last = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr-steps)
        return self.urls[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr+steps, self.last)
        return self.urls[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)