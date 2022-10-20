from inspect import stack
from multiprocessing.sharedctypes import Value


class Stack:
    def __init__(self):
        self.stack= []
        self.minstack=[]
    

    def push(self,val):
        self.stack.append(val)
        if (len(self.minstack)) != 0:
            mymin= min(val, self.minstack[-1])
        else:
            mymin = val
        self.minstack.append(mymin)
        print (self.minstack)
        print(self.stack)


        
    
    def pop(self):
        if len(self.stack)==0:
            pass
        self.stack.pop()

        if len(self.minstack)==0:
            pass
        self.minstack.pop()
        print(self.stack)
        print(self.minstack)


       

    def top(self):
        print (self.stack[-1])
        print (self.minstack[-1])

    def getmin(self):
        print(self.minstack[-1])

        




stack1= Stack()
stack1.push(5)
stack1.push(10)
stack1.push(15)

stack1.pop()
stack1.top()
stack1.getmin()



        
