                       #Function

#With arguments
def greet(name):
  print("Hello "+ name)

greet("krishna")  
 
 #default parameter
def greet(name = "stranger"):
  print("Hello "+ name)

greet()  

#Without Arguments

def intro():
  print("I am Krishna")

intro()  

#Write a program in python to find the greatest number in 3 numbers

def greatestNumber(a,b,c):
  if a == b and b == c:
    print("All numbers are equal",a)
  elif a >= b and a >= c:
    print(a,"is greater")
  elif b >= a and b >= c:
    print(b,"is greater")
  elif c >= b and c >= a:
    print(c,"is greater")

greatestNumber(6,2,0)     

# Write a program to convert celsius to fahreheit

def celsiusToFahreheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  print(fahrenheit," F")

celsiusToFahreheit(0)  

#How do you prevent python print () function to print a new line at the end

def preventPrint():
  print("Hello",end=" ")
  print("Krishna")

preventPrint()                         # print in same line  "Hello Krishna" 

def sumNatural(sum,n):
  while n == 0:
    return sum
  sum += n
  return sumNatural(sum,n-1)

result = sumNatural(0,10)
print(result)              

# Write a function to print the pattern

def pattern(n):
  for i in range(n,0,-1):
    print("*" * i)

pattern(10)          

# Write a python punction to convert inches into cm

def inchesToCm(inches):
  print(inches * 2.54," cm")

inchesToCm(6) 

A = ["krishna","shiva"," vikas "," akshay"]

def listWord(list,word):
  for element in list:
    if element.strip() == word.strip():
      return word.strip() 
    
result = listWord(A,"akshay")  
print(result)                        

def mulTable(n):
  for i in range(1,11):
    print(n*i)

mulTable(19)       

#Snake , Water and Gun Game

def snakeWaterGunGame():
  import random
  randomNumber = random.random()*3
  userChoice = input("Enter your choice: ").capitalize()
  if randomNumber >= 0 and randomNumber < 1:
    computerChoice = "Gun"
  elif randomNumber >= 1 and randomNumber < 2:
    computerChoice = "Snake"  
  elif randomNumber >= 2 and randomNumber < 3:
    computerChoice = "Water" 

  if userChoice == "Snake"  and computerChoice == "Water" or userChoice == "Gun"  and computerChoice == "Snake" or userChoice == "Water"  and computerChoice == "Gun":
    print("You won! computerChoice -> ",computerChoice)

  elif userChoice == "Snake"  and computerChoice == "Gun" or userChoice == "Gun"  and computerChoice == "Water" or userChoice == "Water"  and computerChoice == "Snake":
    print("You loss! computerChoice-> ",computerChoice) 

  elif userChoice == computerChoice:
    print("Tie! computerChoice -> ",computerChoice)

  else:
    print("Wrong input")  

snakeWaterGunGame()  