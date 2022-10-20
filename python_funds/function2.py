def countdown(x):
    for i in range(x,-1,-1):
        print(i)
countdown(5)



def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))


def first_plus_length(list1):
    z = list1[0]+list1[len(list1)-1]
    return z
x = first_plus_length([1,2,3])
print(x)



def greater(list3):
    list4 = []

    for i in range(0,len(list3)):
        if list3[i]>list3[1]:
            list4.append(list3[i])
    if len(list4) >= 2:
        print(len(list4))
        return list4
        
    else:
        print(False)
        
    

print(greater([1,2,5]))


def length_that_value(size,value):
    listnew=[]

    for i in range(size):
        listnew.append(value)

    return listnew


print(length_that_value(6,2))




