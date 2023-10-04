'''
706. Design HashMap
Easy

4556

401

Add to List

Share
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

Constraints:

0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.
'''
class MyHashMap:

    def __init__(self):
        self.m = 1000 # number of buckets
        self.arr = [None]*self.m
        
    def put(self, key: int, value: int) -> None:
        index = key%self.m
        if not self.arr[index]:
            self.arr[index] = [(key, value)]
            return 
        for i, (old_key, old_val) in enumerate(self.arr[index]):
            if old_key == key:
                self.arr[index][i] = (key, value)
                return
        self.arr[index].append((key, value))
            
    def get(self, key: int) -> int:
        index = key%self.m
        if not self.arr[index]:
            return -1
        for old_key, old_val in self.arr[index]:
            if old_key == key:
                return old_val
        return -1

    def remove(self, key: int) -> None:
        index = key%self.m
        if not self.arr[index]:
            return
        for i, (old_key, old_val) in enumerate(self.arr[index]):
            if old_key == key:
                if i == len(self.arr[index])-1:
                    self.arr[index].pop()
                else:
                    self.arr[index][i] = self.arr[index][-1]
                    self.arr[index].pop()
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)