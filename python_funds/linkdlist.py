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

    def deleteNode(self,pos):
        if pos ==0:
            temp =self.head
            self.head = self.head.next
            temp = None
        else:
            current=self.head
            for i in range(pos-1):
                current= current.next
            current.next= current.next.next

   

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
        self.head= prev
    
    def insertatpos(self, pos, value):
        if pos == 1:
            newNode=Node(value)
            newNode.next=self.head
            self.head= newNode
        else:
            current= self.head
            for i in range(pos-2):
                current= current.next
            newNode= Node(value)
            newNode.next=current.next
            current.next=newNode
          


    






list1 = LinkedList()

# node1 = Node("haneen")
# node2 = Node("han")
# node3 = Node("hanz")

# list1.head = node1    
# #   we have to add the next point before adding to next
# list1.head.next = node2
# list1.head.next.next=node3

list1.head = Node("Iron man")
list1.head.next = Node("Dr.Strange")
list1.head.next.next=Node("Thor")
list1.head.next.next.next=Node("Winter Soldier")


# list1.deleteNode(3)


list1.traverse()
# list1.reverse()
list1.insertatpos(2,"Thanos")
list1.traverse()




    
