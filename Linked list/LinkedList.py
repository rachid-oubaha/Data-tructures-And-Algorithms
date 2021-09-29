# Node class
class Node:
   def __init__(self, value=None):
      self.value = value
      self.next = None

# Linked List class
class SLinkedList:
   def __init__(self):
      self.head = None
        
    # This function prints contents of linked list
    # starting from head
   def printList(self):
        temp = self.head
        while (temp):
            print (temp.value)
            temp = temp.next
            
    #Inserting at the Beginning
   def insertAtBegining(self, value):
        temp = self.head
        if(temp is None):
            self.head = Node(value)
            return
        else:
            NewNode = Node(value)
            NewNode.next = self.head
            self.head = NewNode
    
    
    #Inserting at the End
   def insertAtEnd(self, value):
        temp = self.head
        if(temp is None):
            self.head = Node(value)
            return
        else:
            while(temp.next):
                temp = temp.next
            temp.next= Node(value)
    #search
   def search(self, value):
        temp = self.head
        if (temp is None):
            print("Not found")
        while (temp is not None):
            if (temp.value == value):
                print("found")
                return
            temp = temp.next
        print("Not found")
            
        
    
    #delete
   def delete(self, value):
        temp = self.head
        
        if (temp is not None):
            if (temp.value == value):
                self.head = temp.next
                temp = None
                return
            
        while (temp is not None):
            if (temp.value == value):
                prev.next = temp.next
            prev = temp
            temp = temp.next
            
        if(temp is None):
            return
 
