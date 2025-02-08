'''
2349. Design a Number Container System
Solved
Medium
Topics
Companies
Hint
Design a number container system that can do the following:

Insert or Replace a number at the given index in the system.
Return the smallest index for the given number in the system.
Implement the NumberContainers class:

NumberContainers() Initializes the number container system.
void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.
 

Example 1:

Input
["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
Output
[null, -1, null, null, null, null, 1, null, 2]

Explanation
NumberContainers nc = new NumberContainers();
nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
nc.change(2, 10); // Your container at index 2 will be filled with number 10.
nc.change(1, 10); // Your container at index 1 will be filled with number 10.
nc.change(3, 10); // Your container at index 3 will be filled with number 10.
nc.change(5, 10); // Your container at index 5 will be filled with number 10.
nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20. 
nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.
 

Constraints:

1 <= index, number <= 109
At most 105 calls will be made in total to change and find.
'''
class NumberContainers:

    def __init__(self):
        self.ind_num = {}
        self.num_ind = {}
        self.to_remove = {}

    def change(self, index: int, number: int) -> None:
        if index in self.ind_num:
            # print('inside', index, number, self.ind_num, self.num_ind)
            prev_number = self.ind_num[index]
            prev_ind_heap = self.num_ind[prev_number]
            to_remove_heap = self.to_remove.get(prev_number, [])
            heappush(to_remove_heap, index)
            
            while prev_ind_heap and to_remove_heap and prev_ind_heap[0] == to_remove_heap[0]:
                heappop(prev_ind_heap)
                heappop(to_remove_heap)
            
            if prev_ind_heap:
                self.num_ind[prev_number] = prev_ind_heap
            else:
                del self.num_ind[prev_number]
            if to_remove_heap:
                self.to_remove[prev_number] = to_remove_heap
            else:
                if prev_number in self.to_remove:
                    del self.to_remove[prev_number]
            
        self.ind_num[index] = number
        curr_ind_heap = self.num_ind.get(number, [])
        heappush(curr_ind_heap, index)
        self.num_ind[number] = curr_ind_heap
        # print(index, number, self.ind_num, self.num_ind)

    def find(self, number: int) -> int:
        return self.num_ind[number][0] if number in self.num_ind else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)