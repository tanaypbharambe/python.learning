# functions is a group of statements which perform a specific task  u
# if we have to do the same code multiple times .... then we use functions for more easier side to create functn ;
# def anyvariabletonamethefunction(param1,param2,...): ---> definitation of a function, example
# def calc(a,b):    here a and b are called parameters
#     s=a+b
#     print(s)
#     return s

# calc(2,4) ----> 6  this is called recall of function , here 2 and 4 called aarguments
# calc(4,3)----->7 and soo on hence in this case we have to calculate multiple sums hence this is helpful

# def print_hello():
#     print("hello")

# now whenever we will call the function i.e when we use print_hello() it will print hello 
# 
# there are two types of functn , builtin functions and user defined functions
# built in function are like print(),len(),range()  , type()
#user defined functions :
# def cal(a,b):
#     s=a*b
#     print(s)
#     return s   now this is the function made by us to calculate product if we use cal() 

#function to print length of a list

# hero=["hero","adbh","tanay","chatgpt"]
# def le(list):
#     print(len(list))
#     return len(list)

# le(hero)

# function to print a list in a single line :

# def oneline(list):
#     for s in list:
#         print(s,end=" ") ----->end=" " will be helpful to print elements in row otherwise youll get output in coloumn
# oneline(hero)

#function to find the factorial
# def fact(a):
#     n=a
#     f=1
#     for s in range(1,n+1):
#         f*=s
#     print(f)
# call the function


#function to convert usd into inr

# def conv(a):
#     f=a*83
#     print(f)

# here f is inr and a is usd

#function to identify the numbers are even or odd

# def sep(a):
#     if(a%2==0):
#         print("the number is even")
#     else:
#         print("the number is odd")
    
# sep(int(input("input your integer")))



#recursion is when function calls itself repeatedly , every task performed by recursion is performed by loops and vice versa
#example to print n,n-1,n-2......,1

# def show(n):
#     if(n==0): #-----> ending statement
#         return #---->ending statement
#     print(n,end=" ")
#     show(n-1)

# show(5)

#this is recurrsion  here basically whwnever once we recall a function .... it will itself recall ir again becase at last we put show()


#to cal factiorial by recurrtion

# def fact(a):
#     if a == 0 or a == 1:
#         return 1
#     else:
#         return fact(a - 1) * a
# print(fact(5))


#reccursive function to calculate sum of first n natural numbers

# def sum(n):
#     if(n==0):
#         return 0
#     else:
#         return sum(n-1)+n
    
# print(sum(5))
       

#reccursive function to print all elements in a list 
cokker=["kjichadi","chane","rice","daal"]
def elem(list,idx=0):
    if(idx ==len(list)):
        return
    else:
        print(list[idx])
        elem(list,idx+1)

elem(cokker)