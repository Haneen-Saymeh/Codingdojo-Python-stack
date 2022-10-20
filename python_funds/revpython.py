

def palin(list):
    if list == list[::-1]:
        return True
    return False
    
print(palin("radar"))


list1 = "haninz"
print(list1[::-1])
print(list1==list1[::-1])