def biggie_size(list):
    listnew = []
    for i in range(0, len(list)):
        if list[i]>0:
            listnew.append("big")
        else:
            listnew.append(list[i]) 
    return listnew  

print(biggie_size([-1,2,-4]))      


def count_pos(arr):
    count = 0
    for i in range(0, len(arr)):
        if arr[i]>0:
            count= count+1
    arr[len(arr)-1] = count
    return arr
print(count_pos([-1,-2,5,3,-4]))

def sum_total(list):
    sum = 0
    for i in range(0, len(list)):
        sum = sum+list[i]
    return sum

print(sum_total([1,2,3,4]))


def avg(list):
    sum = 0
    aveg = 0
    for i in range(0,len(list)):
        sum = sum + list[i]
    aveg= sum/len(list)
    return aveg

print(avg([1,2,3,4]))


def countlength(list):
    length = len(list)
    return length
print(countlength([1,1,1,5,4]))


def findmin(list):
    min = list[0]
    
    for i in range (0, len(list)):
        if len(list)==0:
            print(False)
        if list[i]< min:
            min = list[i]
    return min

print(findmin([1,2,3]))


def findmax(list):
    max = list[0]
    
    for i in range (0, len(list)):
        if list[i]> max:
            max = list[i]
    return max

print(findmax([1,5,9,-8]))

def ult_an(list):
    sum = 0
    average= 0
    min = list[0]
    max = list[0]
    for i in range (0, len(list)):
        if list [i] <min:
            min = list[i]
        if list[i] > max:
            max = list[i]
        sum=sum+ list[i]
    average= sum/len(list)

    return min, max, sum, average
print(ult_an([1,2,3,4]))

def rev(list):
    list = list[::-1]
        
    return list

print(rev([1,2,3,4,5]))
        



