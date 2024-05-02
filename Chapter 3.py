# Slicing

a = "krishna"
print(a[1:5])
print(a[:4])
print(a[2:])
print(a[2:6:3])
print(a[:-3])
print(a[-6:-2])

#Write a program to display a user entered name followed by good Afternoon.

name = input("Enter your Name:")
print("Good Afternoon Mr.",name)

#Write aprogram to fill the given Template
""" letter = Dear </name>
          You are Selected
          </Date>  """

import datetime
name = input("Enter your Name:")
date = datetime.date.today()
print("Dear",name,"\nYou are Selected\n",date)

#Write a program to detect double spaces in a string

b = "krishna  yadav"
if b.find("  ") > 0:
  print("True")
else:
  print("False")  

#Write a program to replace the string

a = "I am Krishna Yadav"   
print(a.replace("Yadav","Kumar Yadav")) 

# Write a program to use of escape characters

print("Dear Krishna \n\tThis is Python\\\n\tThanks\'") 

# Write a program with use of all strings methods

string = "  krishna Kumar Yadav"

print(len(string))                         #len ()
print(string.endswith("dav"))               #endswith () -> True
print(string.endswith("fdg"))               #endswith () -> False
print(string.startswith("kri"))             #startswith () -> True
print(string.startswith("jfdf"))            #startswith () -> False
print(string.capitalize())                  #capatalize () ->convert first character of string to capital
print(string.lower())                       #lower () -> convert all characters of string to lower
print(string.upper())                       #upper () ->convert all characters of string to upper
print(string.find("mar"))                   #find () -> find character in string with index 
print(string.find("mdfsr"))                 #find () -> find character in string with index not found than return -1
print(string.replace("Kumar",""))           #replace () -> replace oldstring with newstring
print(string.count("a"))                    #count () -> count occurence of character in a string
print(string.strip())                       #strip () -> remove leading and trailing whitespaces 

wordList = ["I","am","Krishna","Kumar","Yadav"]
print(" ".join(wordList))                   #join () -> join the array intos string with seperator " "

wordString = "KKY"
print("-".join(wordString))                 #join () -> seperate each character of string with a seperator "-"  

word = "Krishna Kumar Yadav"
print(word.split())                         #split () -> split string and convert to list if delimetor is not assign 
print(word.split("a"))                      #split () -> split string and convert to list at the given delimeter  








