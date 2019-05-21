# Implement priority queue with O(n) insert and O(1) remove
# Given task and its priority, implement priority queue

class Node:
    def __init__(self, data, rank):
        self.data = data
        self.rank = rank
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None
    
    # O(n) insert
    def insert(self, data, rank):
        newNode = Node(data, rank)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            # smallest rank first
            if newNode.rank < self.head.rank:
                self.head = newNode
                newNode.next = current
            else:
                prev = None
                while current:
                    if newNode.rank < current.rank:
                        # print ("current is ", current.rank)
                        break
                    prev = current
                    current = current.next
                
                prev.next = newNode
                newNode.next = current

    def printPQ(self):
        if self.head == None:
            print ("None")
        else:
            current = self.head
            while current:
                print (current.data, current.rank)
                current = current.next



pq = PriorityQueue()
pq.insert("A", 2)
pq.insert("C", 5)
pq.insert("B", 4)
pq.insert("E", 7)
pq.insert("D", 6)

pq.printPQ()