#loops are used to repet instructions type 1 : while loops and type 2 : for loops
#while loops (while condition "jab tak "")
# a = 1 
# while a<=5:
#     print("hello")
#     a+=1 ---> will print hello 5 times 

#print numbers from 1 to 5 
# i=1
# while i<=5:
#     print(i)
#     i+=1 ---> increases i by 1

#print 5 to 1 
# i=5
# while i>=1:
#     print(i)
#     i-=1 ---> decrease i by 1
#always use stopping condition in loops


#table of 3
# i=1
# while i <=10 :
#     print(3*i)
#     i+=1


# print elements of the following list using a loop 
# list=[1,4,9,16,25,36,49,64,81,100]
# idx=0 #-----> index always starts with 0 and ends with number of elements in list - 1
# while idx <= (len(list)-1):
#     print(list[idx])
#     idx+=1


#break : used to terminate the loop when encounterd


#search a number x in a tuple     called as linear search in programming
# nums=(1,4,9,16,25,36,49,64,81,100)
# x=36
# i=0
# while i<=(len(nums)-1):
#     if(nums[i]==x):
#         print("found at index",i)
#         break
#     else:
#         print("finding...")
#     i+=1


# continue: terminates execution in the current iterationand continues execution of the loop with the next iteration.
# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue ----> acts as skip
#     print(i)
#     i+=1 ----> 0,1,2,4,5



#for loops are used for sequencial travel
# nums=[1,2,3,4,5]
# for a in nums:
#     print(a)

# to traverse in a data type we use for loops 


#to end the for loop we use else ;if we use break in the command dont use else
# str="tanay"

# for char in str:
#     if(char=='n'):
#         print("n found")
#         break
#     print(char)
#     print('END')


#to search for a number x in the tuple using loop:
# tup=(1,2,3,4,5,6,7,8,9)
# x=4
# idx=0
# for num in tup :
#     if(num==x):
#         print("found at index",idx)
#         break
#     idx += 1



#range() : range functions returns a sequence of numbers , starting from 0 (by default) , and increments by 1 (by default)and stops before a specified number
# seq=range(8)
# for i in seq:
#     print(i)

#format is range(start,stop,step)

#pass is a null statement that does nothing , it is used as a placehold for future code.
# for i in range(5):
#     pass
# print("some usefull work is going on")


#program to find the sum of first n numbers (using while)
# n=5
# i=1
# total=0
# while i<=n:
#     total+=i
#     i+=1
# print(total)


#program to find factorial of first n numbers (usning for)(n!)
n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)