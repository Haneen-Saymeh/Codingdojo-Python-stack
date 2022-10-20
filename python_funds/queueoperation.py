class Qeue:
    def __init__(self):
        self.qeue= []
       

    def enq(self,val):
        self.qeue.append(val)
        print (self.qeue)

    def deq(self):
        if len(self.qeue)<=0:
            print("Qeue is empty")
        else:
            self.qeue.pop(0)
            print (self.qeue)

    def deqlast(self):
        self.qeue.pop(-1)
        print(self.qeue)


q1 = Qeue()
q1.enq(5)
q1.enq(3)
q1.enq(15)
q1.enq(6)
q1.enq(7)
q1.deq()
# q1.deqlast()
q1.deq()
q1.deq()
q1.deq()
q1.deq()
q1.deq()