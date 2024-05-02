#Write a python program toadd 2 numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the Second number: ")) 

print("Sum of",a,"and",b," is ",a+b)

#Write a program to find remainder when a number isdivide by 2

number = int(input("Enter the number: "))
print("Remainder of ",number,"is",number%2)

#Write a program in python to check the type of variable from input()

number = int(input("Enter the number: "))
print(type(number))

#Write a program to check the greatest number in between 2 numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the Second number: ")) 
if a > b :
  print(a,"is greater")
elif a < b :
  print(b,"is greater") 
else:
  print("Both are equal")   

#Write a program to find average of 2 numbers enter by user

a = int(input("Enter the first number: "))
b = int(input("Enter the Second number: "))

print("Average of ",a,"and",b,"is",(a+b)/2)

#Write a program to find a square of number enter by user

number = int(input("Enter the number: "))
print("Square of",number,"is",number*number)

#Complex number

a =3 +4j
reall = a.real
imagnery = a.imag
summ = reall + imagnery
print(reall)
print(imagnery)
print(summ)
