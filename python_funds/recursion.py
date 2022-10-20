# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))

# # in recursion we should define base (stopping condition), and we should call the function inside  the function
# def fib(n):
#     if n<=1:        # base, stopping function 
#         return n
#     else:
#         return fib(n-1)+fib(n-2)     #calling the function inside the function!

# print(fib(11))

# def trib(n):
#     if n<=1:        # base, stopping function 
#         return n
#     else:
#         return trib(n-1)+trib(n-2)+trib(n-2)    #calling the function inside the function!

# print(trib(10))

# def trib(n):
#     if n == 0:
#         return 0
#     elif (n == 1 or n ==2) :
#         return 1
#     else :
#         return trib(n-1)+trib(n-2)+trib(n-3)    

# print(trib(3))

def power(n,p):
    
    if p ==0:
        return 1
    elif p ==1:
        return n
    if p <0:
        return 1/n*power(n,p+1)

   
    
    return n*power(n,p-1)
    

print(power(2,3))
print(power(2,-5))









