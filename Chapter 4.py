                                        # List
theList = ["apple", "banana", "orange", "grape",5,34,65,False,True,True]

theList.append(9)                              #addding 9 element to the list
print(theList)                                   

theList.insert(3,"Krishna")                    #insert "krishna" at index 3 of list
print(theList)

theList.remove("grape")                        #remove "grape" from the list
print(theList)

theList.pop(7)                                 #remove element at index 7
print(theList)

theList.reverse()                              #reverse the element of list
print(theList)

print(theList.index("Krishna"))                #check index number of "Krishna"

print(theList.count(True))                     #count the repetation of True


theList = [32,344,432,65,345,4,3,0,566,343,232,45,3,8]

theList.sort()                        #sort the element in ascending order in list and only integers datatype allow
print(theList)  

                                                #Tuple

fruits = ("apple", "banana", "orange", "grape")

print(fruits[1])                       #Accessing tuple
print(fruits.index("grape"))           #check index of elment in tuple
print(fruits.count("apple"))           #Check number of repeation of element in tuple

newFruits = fruits + ("mango",)        #Adding two tuple to modify the previous tuple
print(newFruits)                       #Modifing Tuple  

#Tuple Packing

fruits = "kela","sev","aanar","aam"
print(fruits)
print(type(fruits))

                                               #Exercise

#Write a program to list of fruits entered by user

fruits = []
for fruit in range(7):
  x = input("Enter fruit name")
  fruits.append(x)
print(fruits)  

#Write a program to enter marks of student and sort in list

studentMarks = []
for mark in range(6):
  x = int(input("Enter your marks :"))
  studentMarks.append(x)
studentMarks.sort()  
print(studentMarks)  

#Check that a tuple cannot change 

fruits = ("apple", "banana", "orange", "grape")

try:
  fruits[0] = "kela"
except TypeError as e:
  print(e) 

#Write a program to sum a list

A = [6,6,6,6,6]
sum = 0
for element in A:
  sum += element
print(sum)  

#Write a program to count 0 from the tuple

a =(7,0,8,0,0,0,9)
print(a.count(0))