# default constructor of DEDLL that creates an empty list of size 0 with head and 
# tail pointing to null
class DoubleEndedDoublyLinkedList:
    def __init__(self):
        self.currentSize = None
        self.head = None
        self.tail = None
    
    def insertFront(n):
        # if list is empty
        if self.head == None:
            self.head = n
            self.tail = n
        # one node or more in the list
        else:
            n1 = self.head
            self.head.next = n
            n.next = n1
            n1.prev = n

