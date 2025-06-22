#list is a built in data which stores data values such as; a=54, b=43, c=89 can be float and strings too to store it we use 
# list=[54,43,89] if we print list it will give us the list variable we recently used
# also if we print(list[0]) we will get 54 , list can be changed 
# student=["tanay",18,"jalgaon"]
# print(student[0])
# student[0]="piyush"
# print(student)---> [piyush,18,jalgaon]
#we can slice list too such as for the list we created if print(list[1:2])---> [48,89]
#functions of a list can be used to modify lists {list.function()}
#       list.append(ending index) ==> adds ending index element to an end
#       list.sort() == > sorts in ascending order 
#       list.sort(reverse=True) ==> sorts in descending order
#       list.reverse() ==> reverse the positions of elements
#       list.pop(index) ==> deletes the value of the index
#     to use this functions ;
#    a=[4,3,2,5]
#    a.sort()
#    print(a) ----> [2,3,,4,5] , sorting can be possible in strings also , (alphabetical order)
# tuple is a brother of list , its data type let us create immutable sequence of values just like strings here we just use () instead of []
# tup.index(element)==>returns firsocct urance of an element
# tup.count(element)==>counts occurance of elements 

# program to enter user their 3 favourite movies and store it in a list
a=str(input("enter name of the first movie"))
b=str(input("enter name of the second movie"))
c=str(input("enter name of third movie "))
list=[a,b,c]
print("your favouritte movies are",list)

# palindrome are those  list when we got same order form starting and ending ex. [1,2,3,4,3,2,1]
# to check palindrome list make a copy of a list and reverse it and check reversed copy = origional list {way to solve palindromic questions in python}

#program to check list is palindromic 

a=int(input("enter first integer"))
b=int(input("enter second integer"))
c=int(input("enter third integer"))

list=[a,b,c]

copy_list= list.copy()
copy_list.reverse()


if(copy_list == list):
    print("your list is palindromic")
else:
    print("your list is not palindromic")

#thats it for lec 3