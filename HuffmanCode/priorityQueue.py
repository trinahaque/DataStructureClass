# Implement priority queue with O(n) insert and O(1) remove
# Given task and its priority, implement priority queue

class Node:
    def __init__(self, data, rank):
        self.data = task
        self.rank = rank

class PriorityQueue:
    def __init__(self):
        self.head = None
    
    # O(n) insert
    def insert(self, data, rank):
        newNode = Node(data, rank)


pq = PriorityQueue()
pq.insert("A", 2)