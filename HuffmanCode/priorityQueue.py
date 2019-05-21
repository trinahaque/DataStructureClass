import string

# Implement priority queue with O(n) insert and O(1) remove
# Given task and its priority, implement priority queue

class Node:
    def __init__(self, data=None, rank=None, left=None, right=None):
        self.data = data
        self.rank = rank
        self.next = None
        self.left = left
        self.right = right

class PriorityQueue:
    def __init__(self):
        self.head = None
    
    # O(n) insert
    def insert(self, node):
        if self.head == None:
            self.head = node
        else:
            current = self.head
            # smallest rank first
            if node.rank < self.head.rank:
                self.head = node
                node.next = current
            else:
                prev = None
                while current:
                    if node.rank < current.rank:
                        # print ("current is ", current.rank)
                        break
                    prev = current
                    current = current.next
                
                prev.next = node
                node.next = current
    # O(1)
    def remove(self):
        # when list is empty
        if self.head == None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp


    def oneLeft(self):
        if self.head.next == None:
            return True
        else:
            return False


    def printPQ(self):
        if self.head == None:
            print ("None")
        else:
            current = self.head
            while current:
                print (current.rank)
                current = current.next


class Tree:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right


def frequencyMap(string):
    map = {}
    for char in string:
        if char == " " and "Sp" not in map:
            map["Sp"] = 1
        elif char == " " and "Sp" in map:
            map["Sp"] += 1
        elif char not in map:
            map[char] = 1
        else:
            map[char] += 1
    return map


if __name__ == "__main__":
    stringSample = "SUSIE SAYS IT IS EASY."
    map = frequencyMap(stringSample)
    pq = PriorityQueue()
    tree = Tree()

    for each in map:
        newNode = Node(each, map[each])
        tree = Tree(newNode)
        # print (tree.root)
        pq.insert(tree.root)
        # print (tree.root)
    # pq.printPQ()

    # Second Part
    while not pq.oneLeft():
        node1 = pq.remove()
        # print (node1.data, node1.rank)
        node2 = pq.remove()
        # print (node2.data, node2.rank)
        nodeNew = Node(None, node1.rank + node2.rank, node1, node2)
        # print ("main", nodeNew.rank)
        pq.insert(nodeNew)
    print (pq.printPQ())
    # return pq.remove()




