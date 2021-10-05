class Queue:
    def __init__(self):
        self.queue = list()
# to insert an element
    def enQueue(self,value):
        self.queue.insert(0,value)


    def size(self):
        return len(self.queue)
        
# to remove an element
    def deQueue(self):
        if self.size() > 0:
            return self.queue.pop()
        return "No elements in Queue!"
    
# Node class
class Node:
   def __init__(self, value=None):
      self.value = value
      self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        
    
    def printList(self):
        temp = self.front
        while (temp):
            print (temp.value)
            temp = temp.next
        
    def isEmpty(self):
        return self.front == None
    
    def enQueue(self,value):
        if(self.front is None):
            self.front = self.rear = Node(value)
            return
        newNode = Node(value)
        self.rear.next= newNode
        self.rear = newNode
        
    def deQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        temp = None
        return
    

