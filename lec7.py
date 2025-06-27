#python can be used to perform operations on a file (read and write the data)

#use notes of shraddha didi for files , these notes are incomplete

# types of files : 1 text files (.txt , .docx , .log , etc)    2 Binary files : . mp4 , .mov , .png , .jpeg , etc
# #  ex. file name =sample.txt or doc.docx      mode : r(read mode )  , w(write mode) ,a(append mode), etc 
#we have to open a file before reading or writing .  
# f=open("file_name","mode")

#reading of a file
#f=open("file name","r")
# data=f.read() ----> read whole file             f.readline() ----> reads a line by starting from first
# print(data) ----> print the data of a text file 
#f.close() ----> always close the file

#writing to a fine

# f=open("filename","w")
# f.write("new data") now the file data is changed whenever u open the file and deletes all the past data
# f.close

#r+ mode is used for read and overwrite same w+ do but diff is in r+ no truncate and in w+ there is truncate
#a+ mode is used to read and append and no truncate
#main thing in using these modes are to place pointer , wherever you will place the pointer , changes will happen from there

#with syntax:
# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data) ----> print the data
# using with will automitacally close the file which is good 

#deleting a file :
# using the os module(like a code library)is a file written by another programmerthat generally has a functions we ca use , to U
# import os

#program to replace the string jasa with python in your file
with open("practice.txt","r+") as f:
    data=f.read()

data.replace("java","python") 

#program to searn a word in a file exists or not 
with open("file.txt","r") as f:
    data=f.read()
    if(data.find("word")!= -1):
        print("FOUND")
    else:
        print("not found")


#function to find in which line of the file does the word "word" occur first. print -1 if not found

def check_line():
    word="word"
    data=True
    line_no=1
    with open("file.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    
    return -1



#from a file containing numbers seperated by comma , print the count if even numbers . 
with open("file.txt","r") as f:
    data=f.read()

    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            print("count")
        else:
            print("odd")
   

