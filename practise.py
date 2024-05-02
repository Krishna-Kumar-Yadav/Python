""" import copy

original_list = [1, [2, 3], 4]
copied_list = copy.deepcopy(original_list)

copied_list[0] = 5  # Modify top-level element
copied_list[1][0] = 76  # Modify nested list

print(original_list)  # Output: [1, [0, 3], 4]
print(copied_list) 

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)
print(type(squared_numbers))  """

#Discuss the various string operation n python

#Concatanation

a = "krishnakumaryadav"
b = "K-G "
c = "K-K"

""" print(c + " likes " + b)

#Repetion

#print(b * 5)

#Indexing

print(a[3])
print(a[-10])

#slicing

print(a[:6])
print(a[6:])
print(a[6:12])

#length

print(len(a))  

#membership

print("krish" in a)
print("krish" not in a)     

#case conversion

print(a.capitalize())
print(a.upper())
print(a.lower())         

#spliting and joining

d = [char*2 for char in a]
print(d)
e = " ".join(a)
print(e)        

print(a.replace("kumar"," "))
print(a.find("kumar"))
print(a.find("kdjf"))      

#set operation in list

A = [1,2,3,4,5]
B = [4,5,6,7,8,9]
C = set(i for i in A)
D = set(j for j in B)



print(C)
print(D)

 print(C | D)
print(C & D)
print(C - D)
print(C ^ D) 

#Write a program to check list is monotonic or not


def monotonicCheck(A):
  def ascCheck(A):
    for number in range(len(A)-1):
      if A[number] > A[number+1]:
        return False
    return True

  def descCheck(A):
    for number in range(len(A)-1):
      if A[number] < A[number+1]:
        return False
    return True


  if ascCheck(A)  or descCheck(A):
    print("given list is monotonic")

  else:
    print("given list is not monotonic")  

B = [1,2,3,4,5,6,7,8,9,12]
C = [9,8,7,6,5,4,3,2,1,10]    


#write a program to check the prime number

def primeCheck():
  n = int(input("Enter the number : "))
 
  def prime(n):
    if n >1:
      for i in range(2,n):
        if n % i == 0:
          return False
      return True
    else:
      print("Number less than 2 cannot be taken to check prime number")  

  if prime(n):
    print(n,"is prime number")
  else:
    print(n,"is not prime number")   


#Write a program to find factorial usin recursion


def factorial(n):
  product = 1
  def factor(n):
    nonlocal product
    if n > 1:
      product *= n
      return factor(n-1)
    else:
      return product
  result = factor(n)    
  print(result)



def factoria(n):
    if n == 0:
        return 1
    else:
        return n * factoria(n-1)

# Test the factorial function
result = factoria(0)
print("Factorial of 5 is:", result)  

#Write a program to sort a list of tuple based on the second element of each tuple


def sortListOfTuples(A):
  B = []
  while A:
    minTuple = A[0]
    for tuple in A:
      if tuple[1] < minTuple[1]:
        minTuple = tuple
    B.append(minTuple)
    A.remove(minTuple)

  print(B)  

S = [(1,2,6,7),(1,0,454,54),(5,1,567,9),(10,5,776,2),(2,1,34,7),(10,9,43,2)]

#Write a program to check a string in anagramor not

def anagramCheck():
  anagramList = []
  string = input("Enter the anagram string :")
  anagramString = input("Enter the anagram string :")

  for char in anagramString:
    anagramList.append(char)

  for char in anagramString:
    if string.find(char) == -1:
      return False
  return True  


if anagramCheck():
  print("It is anagram ") 
else:
  print("It is not anagram")   


#Write a program to generate fibonaci series upto n terms

def fibonaci(n):
  first = 0
  second = 1
  sum = 0
  print(0)
  print(1)
  for i in range(n-3):
    sum = first + second
    print(sum)
    first = second
    second = sum

#Write aprogram to reverse a string using recursion

def stringReverse(string):
  reverseString = ""
  def reverse(n):
    nonlocal reverseString
    if n >= 0:
      reverseString += string[n]
      return reverse(n-1)
    else:
      return reverseString
    
  return reverse(len(string)-1)
    
        

n = input("Enter string:")
result = stringReverse(n)
print(result)                        

#write a program to check frquency of each word in atext file

def wordFrequency(filepath, newFile):
    word_freq = {}
    with open(filepath, "r") as file:
        content = file.read()
        words = content.split()
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    with open(newFile, "w") as newfile:
        for word, freq in word_freq.items():
            newfile.write(f"{word}: {freq}\n")



def palindrone(n):
    for i in range(len(n)-1//2):
        if n[i] != n[-i-1]:
            return False
    return True     
     
if palindrone(151):
    print("palindrone")   
else:
    print("Not palindrone")  


def palindrone(n):
    string = str(n)
    reverseString = ""

    for i in reversed(string):
        reverseString += i

    if string == reverseString :
        print("palindrone")   
    else:
      print("Not palindrone")             

            

palindrone(11111)        """

names = ["krishna", "khushi", "akshay"]
ages = [30, 25, 35]
salary = [1000000,100000,1000000]
for name, age,salary in zip(names, ages,salary):
    print(name, age,salary)





