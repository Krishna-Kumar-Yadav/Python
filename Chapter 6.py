                                 #Conditional statements

# Write a program to print yes when the age entered by the user is greater th=an and equal to 18

age = int(input("Enter your age: "))
if age >= 18:
  print("YES")
else:
  print("NO")   

#Write a progarm to check the greatest of 4  number by user

a = int(input("Enter number first: "))
b = int(input("Enter number second: "))
c = int(input("Enter number third: "))
d = int(input("Enter number fourth: "))

if a == b and b == c and c ==d:
  print("All numbers are Equal",a)  
elif a >= b and a >= c and a >= d:
  print(a,"is greater")
elif b >= a and b >= c and b >= d:
  print(b,"is greater")  
elif c >= b and c >= a and c >= d:
  print(c,"is greater")  
elif d >= a and d >= c and d >= b:
  print(d,"is greater")   

#Write a program to find out the whether a student is pass or fail if it requires total 40% and atleast 33% in each subject to pass Assume 3 subjects and total marks as an input from the user.

hindi = int(input("Enter your marks in hindi :"))
english = int(input("Enter your marks in english :"))
math = int(input("Enter your marks in math :"))

hindiPercentage = (hindi * 100)/100
englishPercentage = (english * 100)/100
mathPercentage = (math * 100)/100

totalPercentage = ((hindi + english + math)*100)/300

if hindiPercentage < 33:
  print("You are fail in hindi.")
if englishPercentage < 33:
  print("You are fail in English.")
if mathPercentage < 33:
  print("You are fail in math.")   
if totalPercentage < 40:
  print("Overall you are fail \n\t Try next time !")  


# Detect spam containing keywords

x = input("Enter your offer :")
if x == "Click this" or x == "Buy Now" or x == "Make a lot of money" or x == "you won money":
  print("Alert\n\tSPAMS")  

# Write a program to detect the length of username should be the graeter than 10 characters  

username = input("Enter username :")
if len(username) < 10:
  print("username should be 10 or more than 10 characters")      

# Write a program to find the given name is present in lst or not

family = ["krishna","shiva","bholu","shubham","mansi","pooja","dheeraj","ritik","manvi","satyam"]
x = input("Enter your name:")

if x not in family:
  print("Sorry ! You are not the family member") 
  

#Write a program to calcculate the grade from grade chart
  
marks = int(input("Enter your marks: "))  
if marks >= 90 and marks <= 100:
  print("Grade : Excellent")
elif marks >= 80 and marks < 90:
  print("Grade : A")  
elif marks >= 70 and marks < 80:
  print("Grade : B")  
elif marks >= 60 and marks < 70:
  print("Grade : C")  
elif marks >= 50 and marks < 60:
  print("Grade : D")  
elif marks < 50:
  print("Grade : F") 

# Write a program in python to find out  the given post is taking about "krishna" or not  
  
post = input("Enter the post : ")

if post.find("krishna") >= 0:
  print("Yes ! it taking about Krishna")
else:
  print("Ohh! sorry it didn't contain krishna")  
