
# default constructor of a node in a doubly linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

# default constructor of DEDLL that creates an empty list of size 0 with head and 
# tail pointing to null
class DoubleEndedDoublyLinkedList:
    def __init__(self):
        self.currentSize = 0
        self.head = None
        self.tail = None
    
    
    # Time Complexity: Constant
    # Space Complexity: Constant
    # Insert a new node in front of the head
    def insertFront(self, n):
        # if list is empty
        if self.head == None:
            self.head = n
            self.tail = n
        # one node or more in the list
        else:
            n1 = self.head
            self.head = n
            n.next = n1
            n1.prev = n
        self.currentSize += 1
    
    
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    # Insert a new node after the tail
    def append(self, n):
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        self.currentSize += 1


    # Time Complexity: O(n) --> traverses the whole list
    # Space Complexity: O(1)
    # Search for specific data in the list
    def search(self, n):
        if self.head == None:
            return None
        else:
            current = self.head
            while current:
                if current.data == n.data:
                    return current
                current = current.next
            return None


    # Time Complexity: O(n)
    # Space Complexity: O(1) or constant
    # Update a node in the list
    def update(self, o, n):
        if self.head == None:
            return False
        else:
            current = self.head
            while current:
                if current.data == o.data:
                    o.data = n.data
                    return True
                current = current.next
            return False


    # Time Complexity: O(n)
    # Space Complexity: Constant
    # Delete a node from the list
    def delete(self, n):
        # empty list
        if self.head == None:
            return False
        # only one node in the list and that has to be deleted
        elif self.head.data == n.data or self.tail.data == n.data and self.head.next == None:
            self.head = None
            self.tail = None
            self.currentSize -= 1
            return True
        # if the head value needs to be deleted
        elif self.head.data == n.data:
            self.head = self.head.next
            # ask Phil if the prev needs to be reset
            self.head.prev = None
            self.currentSize -= 1
            return True
        # if the tail is deleted
        elif self.tail.data == n.data:
            self.tail = self.tail.prev
            self.tail.next = None
            self.currentSize -= 1
            return True
        else:
            current = self.head
            # Time: O(N)
            while current:
                if current.data == n.data:
                    prev = current.prev
                    next = current.next
                    prev.next = next
                    next.prev = prev
                    self.currentSize -= 1
                    return True
                current = current.next
            return False
                    
        
    #-------------------- Print Fuctions -------------------
    # prints current size of the doubly linked list
    def printSize(self):
        print ("The size of the list is ", self.currentSize)

    # prints head of the doubly linked list
    def printHead(self):
        if self.head == None:
            print ("Empty List")
        else:
            print ("The data value at head is ", self.head.data)

    # prints tails of the link
    def printTail(self):
        if self.head == None:
            print ("Empty List")
        else:
            print ("The data value at tail is ", self.tail.data)

    # printing the whole list starting from the head
    def printForward(self):
        if self.head == None:
            print ("Empty List")
        else:
            print ("Print forward")
            current = self.head
            while current:
                print (current.data)
                current = current.next
    
    # printing the entire list starting from the tail
    def printReverse(self):
        if self.head == None:
            print ("Empty List")
        else:
            print ("Print Reverse")
            current = self.tail
            while current:
                print (current.data)
                current = current.prev

    
    #--------------- Extended Functions ------------------
    # What to do with even or odd list?
    # print the data of the middle node
    def printMiddle(self):
        # empty list
        if self.head == None:
            print ("Empty List")
        # only one node, print value of the node
        elif self.head.next == None:
            print (self.head.data)
        else:
            middle = int(self.currentSize/2)
            current = self.head
            count = 1
            # prints out middle node value of a list with more than one node
            while current:
                if count == middle:
                    return current.next.data
                current = current.next
                count += 1


    # Time Complexity: O(n) --> traversing through the entire list
    # Space Complexity: O(n) --> storing all nodes in the dict
    def removeDuplicates(self):
        if self.head == None or self.head.next == None:
            print ("Empty list")
        else:
            dict = {}
            current = self.head
            while current:
                if current not in dict:
                    dict[current] = 1
                else:
                    prev = current.prev
                    next = current.next
                    if current.next:
                        prev.next = next
                        next.prev = prev
                    # if the last value is None
                    # do I need to reset the None pointer?
                    else:
                        prev.next = None
                        self.tail = prev


    # Time Complexity: 
    # Space Complexity: 
    # Delete all nodes in the DEDLL
    def deleteAll(self):
        # Empty list
        if self.head == None:
            print ("Empty list")
        # only one node
        elif self.head.next == None:
            print (self.head.data)
            self.head = None
            self.tail = None
            self.currentSize -= 1
        # multiple node
        else:
            current = self.head
            while current:
                print (current.data)
                next = current.next
                if next:
                    current.next = None
                    next.prev = None
                    current = next
                else:
                    self.head = None
                    self.tail = None
                self.currentSize -= 1

    
    # reverse a doubly linked list
    # Time Complexity: 
    # Space Complexity: 
    def reverse(self):
        if self.head == None:
            # print ("Empty List")
            return None
        elif self.head.next == None:
            # print (self.head.data)
            return self.head
        else:
            current = self.head
            next = current.next
            self.tail = current
            self.tail.next = None
            while next:
                newNext = next.next
                next.next = current
                current.prev = next
                current = next
                next = newNext
            self.head = current
            self.head.prev = None
               

            
# testing reverse function
node1 = Node(6)
node2 = Node(2)
node3 = Node(5)
node4 = Node(3)
dedll = DoubleEndedDoublyLinkedList()
dedll.append(node1)
dedll.append(node2)
dedll.append(node3)
dedll.append(node4)
dedll.printHead()
dedll.printTail()
dedll.printForward()
dedll.printReverse()
print ("After reversing the list")
dedll.reverse()
dedll.printHead()
dedll.printTail()
dedll.printForward()
dedll.printReverse()


# n = Node(5)
# n2 = Node(2)
# n3 = Node(7)
# dedll = DoubleEndedDoublyLinkedList()
# dedll.printSize()
# dedll.printHead()
# dedll.printTail()
# dedll.insertFront(n)
# dedll.insertFront(n2)
# dedll.printSize()
# dedll.printHead()
# dedll.printTail()
# dedll.append(n3)
# dedll.printTail()
# dedll.printForward()
# dedll.printReverse()
