

# def isbalanced(string):
#     stack=[]
#     for i in string:
#         if i =='(':
#             stack.append(i)
#         elif i == ')':
#             if len(stack) != 0:
#                 stack.pop()
#             else:
#                 return 'unbalanced'
#     if len(stack)==0:
#         return 'balanced'


            


def isbalanced(string):
    stack=[]
    for i in string:
        if i =='(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                return 'unbalanced'
    if len(stack)==0:
        return 'balanced'
    else:
        return 'not balanced'

str="hsb((km_jn))"
print(isbalanced(str))

            


def isbalancedtwo(string):
    open = ['(', '{','[']
    close=[')','}',']']
    stack=[]
    for i in string:
        if i in open:
            stack.append(i)
        elif i in close:
            index= close.index(i)
            if stack [len(stack)-1]== open[index]:
                stack.pop()
            else:
                return 'unbalanced'
    if len(stack)==0:
        return 'balanced'
    else:
        return 'not balanced'

str2="hsb(({[km_jn]}))"
print(isbalancedtwo(str2))



            




