from LinkedList import *


list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("fri")
# Link first Node to second node
list1.head.next = e2

# Link second Node to third node
e2.next = e3

# Link third Node to fourth node
e3.next = e4

#to print contents of linked list
list1.printList()

#delete
list1.delete("Tue")
list1.printList()
list1.insertAtBegining("Tue")
list1.printList()


list1.printList()

list1.insertAtEnd("sat")
list1.printList()

#search
list1.search("sat")
