class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class Linkedlist:
    def __init__(self):
        self.head = None

    
    def printing(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def insertToHead(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
        else:
            current = Node(value)
            current.next=self.head
            self.head=current


    def delete_head(self):
        temp = self.head
        self.head= self.head.next
        temp = None


    def insertTopos(self, value,pos):
        if pos ==1:
            current = Node(value)
            current.next= self.head
            self.head=current
        else:
            current = self.head
            
            for i in range(pos-2):
                current=current.next
            newnode =Node(value)
            newnode.next=current.next
            current.next=newnode

    def  addtoTail(self, value):
        current = self.head
        while current.next is not None:
            current= current.next
        NewNode= Node(value)
        current.next=NewNode

    def delete_tail(self):
        current=self.head
        while current.next.next is not None:
            current = current.next
        lastNode = current.next
        current.next=None
        lastNode= None

    def sizeof(self):
        current = self.head
        total = 0
        while current is not None:
            total = total +1
            current = current.next
        return total

    def printLinkedList(self):
        current = self.head
        total = 0
        while current is not None:
            total = total+1
            print(current.value)
            current= current.next
        return total



                
                
                

            

list1 = Linkedlist()
list1.head=Node("Tony Stark")
list1.head.next= Node("Thor")
list1.head.next.next=Node("Winter soldier")
list1.insertToHead('Haninz')
list1.insertTopos("thanos",3)
list1.addtoTail('Henno')

# list1.printing()
# print(list1.sizeof())

# print(list1.printLinkedList())
# list1.delete_head()
# print(list1.printLinkedList())

list1.printing()

    




        
