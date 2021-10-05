from Queue import *


#for array 
queue = Queue()
queue.enQueue("A")
queue.enQueue("B")
queue.enQueue("C")
print(queue.size())
print(queue.queue)
print(queue.deQueue())
print(queue.deQueue())
print(queue.size())
queue.enQueue("A")
queue.enQueue("B")
queue.enQueue("C")
print(queue.size())

#for linked list
qlist = QueueLinkedList()
qlist.enQueue("A")
qlist.enQueue("B")
qlist.enQueue("C")
print("before delete")
qlist.printList()
qlist.deQueue()
qlist.deQueue()
print("after delete")
qlist.printList()
qlist.deQueue()
qlist.deQueue()
