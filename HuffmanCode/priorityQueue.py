import string

# Implement priority queue with O(n) insert and O(1) remove
# Given task and its priority, implement priority queue

class Node:
    def __init__(self, data=None, rank=None, left=None, right=None):
        self.data = data
        self.rank = rank
        self.next = None
        
class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0
    
    # O(n) insert
    def insert(self, tree):
        # print ("node is")
        node = Node(tree)
        # print (node.data.root.rank)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            # smallest rank first
            if node.data.root.rank < self.head.data.root.rank:
                self.head = node
                node.next = current
            else:
                prev = None
                while current:
                    if node.data.root.rank < current.data.root.rank:
                        # print ("current is ", current.rank)
                        break
                    prev = current
                    current = current.next
                
                prev.next = node
                node.next = current
        self.size += 1
    # O(1)
    def remove(self):
        # when list is empty
        if self.head == None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.size -= 1
            return temp


    def oneLeft(self):
        if self.head.next == None:
            return True
        else:
            return False


    def printPQ(self):
        # print ("head ", self.head)
        if self.head == None:
            print ("None")
        else:
            current = self.head
            while current:
                # print ("printing", current.data.root.data, current.data.root.rank)
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
        # print(newNode.data, newNode.rank)
        tree = Tree(newNode)
        # print (tree.root.data, tree.root.rank)
        pq.insert(tree)
    pq.printPQ()
    # print (pq.size)

    # 2nd Step
    print ("2nd Step")
    while pq.size > 1:
        node1 = pq.remove()
        node2 = pq.remove()
        # print (node1.data.root.rank, node2.data.root.rank)
        node3 = Node("", node1.data.root.rank + node2.data.root.rank)
        # print (node3)
        tree3 = Tree(node3, node1.data.root, node2.data.root)
        # print (tree3.left.data, tree3.left.rank)
        pq.insert(tree3)
    # print (pq.size)
    # pq.printPQ()
    # print (pq.head.data.root.rank)
    print (pq.head.data.root.rank, pq.head.data.left.rank, pq.head.data.left.data)

        


# output
# 10, 01111, 10, 110, 1111, 00, 10, 010, 1110, 10, 00, 110, 10, 00, 1111, 010, 10, 1110, 01110

