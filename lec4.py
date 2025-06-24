# # dictionary are used to store data values in key:values pairs , unorderd , mutable (changable)
# dict = {
#     "name": "Tanay",
#     "age" : 17,
#     "employment":"unemployed",
#     "subjects":["python","machine learning","adrunio"]
# }
# print(type(dict))
# #there is no order in dictionary and cant create duplicate keys
# print(dict["name"])
# print(dict["age"])
# print(dict["employment"])
# print(dict["subjects"]) 
#     #this will give us outputs in a coloumn and print(dict)--> in row
#  to replace keys , 
#  dict["age"]=18
#  print(dict)
# nested dictionary:
# student={
#      "name":"Piyush",
#      "subject": {
#          "phy": 98,
#          "chem":92,
#          "maths":99
#      },
#  }
#print(student.items()) 
# print(len(student)) #---> 2
# print(student.keys()) #----> name and subject
# print(student.values()) 
# # we can store dict in list
# print(list(student.values())) 
 # and many more functions
# print(student["name1"]) #error
# print(student.get["name1"]) #no eeor---> none helps us if we made any mistake in code it will run the after code too


#sets : set is the collection of the unorderd items , each element in the set must be unique and immutable 
# collection = {1,2,3,"hello",4,8.29,True} is a set , it is always unorderd
#duplicated values are not allowed in set such as {2,2,2,"hello","hello }"  #empty set = set{}

# set.add(element) ----> adds an elements
# set.remove(element) ----> removes an elents 

# note that , sets are mutable , elements are immutable....

# set.clear() ---> empties the set
# set.pop() ----> removes an random values

# cant add the element which already exists and cant remobe an element which dosent exists

# set1.union(set2) ---> combines both set values and returns new
# set1.intersection(set2)---->combines common values and returns new


#project to enter marks of three subjects and store in the dictonary.to start with empty dictionary and add one by one.
# marks={}
# print(marks)
# a=float(input("enter marks for subject 1"))
# marks.update({"subject1":a})
# print(marks)
# b=float(input("enter marks for subject 2"))
# marks.update({"subject2":b})
# print(marks)
# c=float(input("enter marks for subject3"))
# marks.update({"subject3":c})
# print(marks)


#seperate 9 and 9.0 ina set
# set={"9",9.0}
#  #or
set={
    ("float",9.0),
    ("int",9)
}
print(set)