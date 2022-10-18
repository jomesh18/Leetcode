'''
Task Scheduler

Solution
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        ans = 0
        max_occurance = max(count.values())
        no_of_maxs = sum(1 for v in count.values() if v == max_occurance)
        part_count = max_occurance-1
        gap_in_one_part = n-(no_of_maxs-1)
        total_gaps = part_count * gap_in_one_part
        available_tasks = len(tasks)-no_of_maxs*max_occurance
        idles = max(0, total_gaps-available_tasks)
        return idles+len(tasks)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time, heap = 0, []
        for k, v in Counter(tasks).items():
            heappush(heap, (-v, k))
        while heap:
            temp = []
            for _ in range(n+1):
                if heap:
                    occur, eve = heappop(heap)
                    if occur != -1:
                        temp.append((occur+1, eve))
                time += 1
                if not heap and not temp: break
            for item in temp:
                heappush(heap, item)
        return time