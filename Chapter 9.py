""" """ # File Handling

file = open("testing.txt","r")
content = file.read()                       #Entire file read
content = file.readlines()                 #['hello\n', 'krishna\n', 'kumar\n', 'yadav'] 
content = file.readline()
print(content) 

#write a program to find a word in python from a file

with open("testing.txt","r") as file:
  content = file.read()
  if content.find("krishna") != -1:
    print("find") 

#Write a program to update score in file of a game
    
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

  def update_line_in_file(file_path, line_number, new_content):
    with open(file_path, 'r') as file:
      lines = file.readlines()

    if 0 < line_number <= len(lines):
      lines[line_number - 1] = new_content + '\n'  

      with open(file_path, 'w') as file:
        file.writelines(lines)

    else:
        print(f"Line number {line_number} is out of range.")

  won = 0
  loss = 0
  tie = 0  
    
  if userChoice == "Snake"  and computerChoice == "Water" or userChoice == "Gun"  and  computerChoice == "Snake" or userChoice == "Water"  and computerChoice == "Gun":
    print("You won! computerChoice -> ",computerChoice)
    won += 1
    content = f"won : {won}"
    update_line_in_file("testing.txt", 1, content)

  elif userChoice == "Snake"  and computerChoice == "Gun" or userChoice == "Gun"  and computerChoice == "Water" or userChoice == "Water"  and computerChoice == "Snake":
    print("You loss! computerChoice-> ",computerChoice) 
    loss += 1
    content = f"loss : {loss}"
    update_line_in_file("testing.txt", 2, content)

  elif userChoice == computerChoice:
    print("Tie! computerChoice -> ",computerChoice)
    tie += 1
    content = f"tie : {tie}"
    update_line_in_file("testing.txt", 3, content)

  else:
    print("Wrong input")       

snakeWaterGunGame() 

# Write a program to generate multiplication table from 2 to 20 and write it to the different files in a folder for a 13 year old

def tableTwoToTwenty(folderPath):

  for file in range(2,21):
    with open(f"{folderPath}/table{file}.txt","w") as tableFile:
      for i in range(1,11):
        tableFile.write(f"{file} * {i} = {file * i}\n")

tableTwoToTwenty("/home/krishna/Desktop/python/tables")    

# Write a program to replace "kk" and insted of it update it to "krishna" 

def updateWord(oldWord,newWord,filePath):
  with open(filePath,"r") as file:
    content = file.read()
    if content.find(oldWord) != -1:
      with open(filePath,"a+") as updateFile:
        index = content.find(oldWord)
        content[index] = newWord
        updateFile.write(newWord)
    else:
      print("Word not find . \n")  

updateWord("kk","krishna","testing1.txt")     

#Find longest common Prefix

def longestCommonPrefix(lst):
    sortedLst = sorted(lst,key=len)
    length = len(sortedLst[0])
    lengthArray = len(sortedLst)
    
    for i in range(length):
        for j in range(lengthArray - 1):
            if lst[j][i] != lst[j+1][i]:                
              return lst[j][:i]   
    return lst  
         
      
A = ['abacdd3434','abacd','abacejhjffd']
print(longestCommonPrefix(A)) 

#Write aprogram in python to find a particular word in a file.

with open("testing1.txt","r") as file:
  content = file.read()
  if content.find("erger") != -1:
    print("find")  

#Write a program to check a integer is prime or not

def checkPrime():
  n = int(input("Enter the integer: "))
  if n <= 1:
    print("only integer greater then 1 can be the prime number.")
  else:
    for element in range(2,n-1):
      if n % element == 0:
        print("not prime") 
        return False

    if True:
      print("prime number")

checkPrime()            

#Write a program to update the word from the file

with open("testing1.txt","r+") as file:
  content = file.read()
  word = "kk"
  if word in content:
    file.seek(0) 
    updatedContent = content.replace(word,"love")
    file.write(updatedContent)


#Write a program to censor words in a lst 

def censorWords(filePath,censorWords):
  with open(filePath,"r+") as file:
    content = file.read()
    for word in censorWords:
      if word in content:
        file.seek(0)
        updateWord = content.replace(word ,"#"*len(word))
        file.write(updateWord)

censorWords("testing1.txt",["love","K-G"])        


# Write a program to check python word in log file

def wordCheckFile(filePath,word):
  with open(filePath,"r") as file:
    content = file.read()
    if word in content:
      print("find")
    else:
      print("not find")

wordCheckFile("test.log","python") 


#Write a program to check the palindrone number

def checkPalindrone():
  n = int(input("Enter the number: "))
  stringNum = str(n)
  oppositeString = ''
  for i in reversed(stringNum):
    oppositeString += i
  if stringNum == oppositeString:
    print("palindrone")
  else:
    print("not palindrone")  

checkPalindrone()  
     


#Wrie a program to find out the line number of the word in a file

def lineNumberCheckOfWord(filePath,word):
  with open(filePath,"r") as file:
      for lineNumber ,line in enumerate(file,start=1):
        if word in line:
          return lineNumber

  return "not find"

print(lineNumberCheckOfWord("testing1.txt","KG"))  

#Write a program to make copy of text file

def copyFileContent(oldFilePath,newFilePath):
  with open(oldFilePath,"r") as oldFile:
    oldContent = oldFile.read()
    with open(newFilePath,"r+") as newFile:
      newFile.write(oldContent)

copyFileContent("testing1.txt","testing.txt")      


#Write a program to find out the content of file is identical or match to another file

def identicalContent(oldFilePath,newFilePath):
  with open(oldFilePath,"r") as oldFile:
    oldContent = oldFile.read()
    with open(newFilePath,"r") as newFile:
      newContent = newFile.read()
      if oldContent == newContent:
        return "content similar"
      else:
        return "content identical"
      
print(identicalContent("testing1.txt","testing.txt") )                

#Write a program to wipe out the data in a file

def wipeDataInFile(filePath):
  with open(filePath,"w") as file:
    file.write("")
wipeDataInFile("testing.txt") 

#Write a program to rename a file

def renameFile(oldFileName,newFileName):
  import os 
  os.rename(oldFileName,newFileName)

renameFile("testing.txt","fantastic.txt")  
      

