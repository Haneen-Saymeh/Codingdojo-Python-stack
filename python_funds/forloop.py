for x in range(0,151):
    print(x)

for y in range(5,1001,5):
    print(y)

for i in range(1,1001):
    if (i % 10 == 0):
        print("Coding Dojo")
    elif (i %5 ==0):
        print("Coding")
    else:
        print(i)

total_odds = 0
for z in range(0, 500001):
    if (z %2 != 0):
        total_odds = total_odds+z

print(total_odds)

for t in range(2018, 0 , -4):
    print(t)


low_num =5
high_num= 21
mult = 5
for w in range(low_num,high_num):
    if w % mult ==0:
        print(w)