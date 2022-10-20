
class Qeue:
    def __init__(self):
        self.qeue= []
       

    def push(self,val):
        self.qeue.append(val)

    
    def front(self):
        print(self.qeue[0])

    def contains(self,val):
        for ele in self.qeue:
            if ele== val:
                return True
    
        return False
        
        


q1= Qeue()
q1.push(10)
q1.push(2)
q1.push(3)
q1.push(5)
q1.front()
print(q1.contains(8))
print(q1.contains(5))






        





