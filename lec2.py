#when we use strings we can use() "" and '' and """" )depending on the condition
#escape sequence characters are used to add a tab space or a line space . for next line we use (\n) fot tab space we use (\t)
#to add two strings we say it concatication such as tan + ay = tanay 
#we can define a length of a function by len(str)
# in lengths spaces are also calculated 
#indexing helps us to access characters , it tells us about position of an letter such as  lets take a word 'TANAY' here str(0) will be T
#str(3) will be A 
#string command cant be used to replace the alphabet or a word
#slicing is an acceccing part of strings  like 
# str = "Tanay"
# a=str[1:3] always use square bracket for slicing ... enter starting index - ending index {depending on your slice}
#this will give us "an" which is a slice of tanay , we can calculate indexes backwords too by starting -1 from end 
#functions help us to modify strings
#conditional statements , we use if , elif , else  syntaxes , we have nesting too ///

a=int(input("enter num 1"))
b=int(input("enter num2"))
c=int(input("enter num3"))
if(a>b and a>c):
    print("greatest number is",a)
elif(b>c and b>a):
    print("greatest number is",b)
elif(c>a and c>b):
    print("greatest number is",c)
   