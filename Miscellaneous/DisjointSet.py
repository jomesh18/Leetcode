class DisjointSet:
    node_map = {}
    class Node:
        def __init__(self, data, rank, parent):
            self.data = data
            self.rank = rank
            self.parent = parent

    def __init__(self):
        pass

    def findset(self, val):
        return self.find_set(self.node_map[val]).data

    def find_set(self, node):
        if node.parent == node:
            return node
        node.parent = self.find_set(node.parent)
        return node.parent

    def union(self, val1, val2):
        node1 = self.node_map[val1]
        node2 = self.node_map[val2]

        parent1 = self.find_set(node1)
        parent2 = self.find_set(node2)

        if parent1.data == parent2.data:
            return

        if parent1.rank >= parent2.rank:
            parent1.rank = parent1.rank + 1 if parent1.rank == parent2.rank else parent1.rank
            parent2.parent = parent1
        else:
             parent1.parent = parent2

    def makeset(self, val):
        node = self.Node(val, 0, None)
        node.parent = node
        self.node_map[val] = node

ds = DisjointSet()

for i in range(1, 8):
    ds.makeset(i)

ds.union(1, 2)
print("after 1 2 res is "+str(ds.findset(2)))
ds.union(2, 3)
print("after 2 3 res is "+str(ds.findset(2)))
print("rank of 1 is "+str(ds.node_map[1].rank))
ds.union(4, 5)
print(ds.findset(5))
ds.union(6, 7)
print(ds.findset(7))
ds.union(5, 6)
print(ds.findset(6))
print("rank of 4 is "+str(ds.node_map[4].rank))
print(ds.findset(3))
print(ds.findset(7))
ds.union(3, 7)
print(ds.findset(7))

for i in range(1, 8):
    print(ds.findset(i))
