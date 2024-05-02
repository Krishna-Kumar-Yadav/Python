""" #path = R"C:\\Users\\John\\Documents"

poem = '''    roses are red,\t
Violets are blue,
Sugar is sweet,
And so are you.   '''



#print(len(poem))
#print(poem.capitalize())
#print(poem.lower())
#print(poem.upper())
#print(poem)
#print(poem.strip())
#print(poem.split())
#print(poem.find("are"))
#a = poem.replace("are","love")
#print(a)
#print(poem.count("aree"))


numbers = [1, 2, 3, 4, 5]
squared_numbers = {x: x**2 for x in numbers}
#print(squared_numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


def isEven():
  n = int(input("Enter the number : "))
  if(n%2==0):
    return True
  return False

if not isEven():
  print("got it")
else:
  print("Shit")  
  

 
a = 7
b = 0

print(a & b)
print(a | b)
print(a ^ b)
print(~5)
print(a << b)
print(a >> b)




#1

file = open("testing1.txt","r")

content  = file.read()
if content.find("kky") == -1:
  print("nope")

file.close()

# Write a program to update score in file of a game


def snakeWaterGunGame():
    import random

    randomNumber = random.random() * 3
    userChoice = input("Enter your choice: ").capitalize()
    if randomNumber >= 0 and randomNumber < 1:
        computerChoice = "Gun"
    elif randomNumber >= 1 and randomNumber < 2:
        computerChoice = "Snake"
    elif randomNumber >= 2 and randomNumber < 3:
        computerChoice = "Water"

    def update_line_in_file(file_path, i, lineNumber):
        with open(file_path, "r") as file:
            content = file.readlines()
            a = content[lineNumber-1][i]
            b = int(a) + 1
            if lineNumber == 1:
              c = "won : "+ str(b)
              newcontent = c
              content[lineNumber-1] = newcontent + "\n"
              with open(file_path, "w") as file:
                file.writelines(content)
            elif lineNumber == 2: 
              c = "loss : "+ str(b)
              newcontent = c
              content[lineNumber-1] = newcontent + "\n"
              with open(file_path, "w") as file:
                file.writelines(content)  
            elif lineNumber == 3: 
              c = "tie : "+ str(b)
              newcontent = c
              content[lineNumber-1] = newcontent + "\n"
              with open(file_path, "w") as file:
                file.writelines(content)     

    if (
        userChoice == "Snake"
        and computerChoice == "Water"
        or userChoice == "Gun"
        and computerChoice == "Snake"
        or userChoice == "Water"
        and computerChoice == "Gun"
    ):
        print("You won! computerChoice -> ", computerChoice)
        update_line_in_file("testing1.txt", 6, 1)

    elif (
        userChoice == "Snake"
        and computerChoice == "Gun"
        or userChoice == "Gun"
        and computerChoice == "Water"
        or userChoice == "Water"
        and computerChoice == "Snake"
    ):
        print("You loss! computerChoice-> ", computerChoice)
        update_line_in_file("testing1.txt", 7, 2)

    elif userChoice == computerChoice:
        print("Tie! computerChoice -> ", computerChoice)
        update_line_in_file("testing1.txt", 6, 3)

    else:
        print("Wrong input")


snakeWaterGunGame()

#delete files

def deleteFiles(folderPath):
  import os

  for file in os.listdir(folderPath) :
    os.remove(f"{folderPath}/{file}")

deleteFiles("/home/krishna/Desktop/python/tables")  
#3

def table(folderPath):
  for file in range(2,21):
    with open(f"{folderPath}/table{file}.txt","w") as f:
      for i in range(1,11):
        content = f"{file} x {i} = {file * i}\n"
        f.write(content)

table("/home/krishna/Desktop/python/tables") """

with open("example.txt", "r") as file:
    print(file.tell())  # Print the initial position of the file pointer
    
    # Read the first 5 bytes of the file
    print(file.read(5))
    
    print(file.tell())  # Print the current position of the file pointer
    file.seek(8)
    print(file.tell())

