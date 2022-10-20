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



    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
        self.head= prev



list1 = LinkedList()

list1.head = Node("Iron man")
list1.head.next = Node("Dr.Strange")
list1.head.next.next=Node("Thor")
list1.head.next.next.next=Node("Winter Soldier")


list1.traverse()
list1.reverse()
list1.traverse()
    
