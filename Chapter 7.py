                              #loops

#for loop

for i in range(0,10):
  print("krishna") 

family = ["krishna","shiva","bholu","shubham","mansi","pooja","dheeraj","ritik","manvi","satyam"]
for member in family:
  print(member)


#while loop

family = ["krishna","shiva","bholu","shubham","mansi","pooja","dheeraj","ritik","manvi","satyam"]

i = 0
while i != len(family):
  print(family[i])
  i = i+1
 

#for loop with else

family = ["krishna","shiva","bholu","shubham","mansi","pooja","dheeraj","ritik","manvi","satyam"]

for member in family:
  print(member)
else:
  print("Done")  

#Write a program to print multiplication table of a given number for loop

x = int(input("Enter the number : "))
for i in range(1,11):
  print(x*i) 

# write a program to greet all the person names stored in a list and which starts with S

l = ["harry","sohan","sachin","krishna","riya"]

for name in l:
  if name.find("s") == 0:
    print("Hello !",name)   

#Write a program to print multiplication table of a given number using while loop

x = int(input("Enter the number : "))
i = 1
while i < 11:
  print(i*x)
  i += 1          

#Write a program to check the given number is prime or not

x = int(input("Enter the number : "))
isPrime = True
for i in range(2,x):
  if x % i == 0:
    isPrime = False
    break
if isPrime:
  print("prime")
else:
  print("not prime")    

#Write a program to print first n natural numbers using while loop

n = int(input("Enter the number : "))
i = 1
sum =0
while i != n+1:
  sum += i
  i += 1
print(sum)  

# Write a program to find factorial of given number using for loop

n = int(input("Enter the number : "))
factorial = 1
for i in range(n,1,-1):
  factorial *= i
print(factorial)

#Write a program to print equilateral triangle star pattern

n = int(input("Enter the number : "))

for i in range(1,n+3):
  if i%2 == 0:
    continue
  else:
    print(" " * (n +3 - i),end="")
    print("* " * i)

  
  
 

# Write a progarm to print triangle pattern

n = int(input("Enter the number : "))
for i in range (1,n+1):
  print("*"*i) 

# Write a program to print a rectangle with spik in the middle

n = int(input("Enter the odd number only number : "))   

for i in range(1,n+1):
  if i == int(n/2+0.5):
    print (("*"*int(n/2-0.5)) + " " + ("*"*int(n/2-0.5)))
  else:  
    print("*" * n)    

# Write a program to print multiplication table n order using for loop reverse order

n = int(input("Enter the number:"))

for i in range(10,0,-1):
  print(i*n)
  