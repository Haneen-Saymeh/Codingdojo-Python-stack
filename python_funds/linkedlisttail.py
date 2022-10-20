from multiprocessing.sharedctypes import Value


class Node:
    def __init__(self, value):
        self.value = value
        self.next= None

class LinkedList:
    def __intit__(self):
        self.head = None


    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    

    def insertNodeatTail(self, value):
        if self.head is None:
            self.head =Node(value)

        else:
            current= self.head
            while current.next is not None:
                current= current.next
        current.next = Node(value)


list1 = LinkedList()

# node1 = Node("haneen")
# node2 = Node("han")
# node3 = Node("hanz")

# list1.head = node1    
# #   we have to add the next point before adding to next
# list1.head.next = node2
# list1.head.next.next=node3

list1.head = Node("Amin")
list1.head.next = Node("Haneen")
list1.head.next.next=Node("Hanz")
list1.insertNodeatTail("sol")
list1.insertNodeatTail("Tony Stark")
list2 = LinkedList()
list2.insertNodeatTail("Haniiiinz")


list1.traverse()
      
        

        
