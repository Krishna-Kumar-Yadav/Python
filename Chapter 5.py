                                        #Dictionary

a = {
  "name" : "krishna",
  "age" : 19,
  "gender" : "male",
  "affair" : False,
  "bestFriend" : "kk",
  "favouriteFood" : ["fresh-dahi","doodh"],
  "favouriteGod" : ("bhagwan-narayan","bhagwan-shiva"),
  "friends" : {
    "college" : "none",
    "home" : "none",
  }
}
print(a["name"])
print(a["affair"])
print(a["favouriteFood"][1])
print(a["favouriteGod"][1])
print(a["friends"]["college"])

#Dictionary Methods

print(a.items())                                     #print all the key-value pair of the dictionary
print(a.keys())                                      #print all the keys of dictionary
print(a.values())                                    #print all the values of the dictionary
print(a.get("friends"))                              #fetch the value from the key
print(a.popitem())                                   #delete last assign key-pair of the dictionary and show value
a.pop("affair")                                      #delete the value with the key use in the dictionary
print(a)
a.update({"friends":"riya"})                         #update the value of the key and can be add another key-value in dictionary
print(a)
a.clear()                                            #delete all the key-values from the dictinary and make it empty
print(a)

#Dictionary Comprehension

numbers = [1, 2, 3, 4, 5]
squared_numbers = {x: x**2 for x in numbers}
print(squared_numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



                                                      #Set

#creating a set

  #method1
KK = {2,3,54,54,"fjkhf"}
print(KK)                  #output -> {2, 3, 54,'fjkhf'}

  #method2
KKK = set([2,3,54,54,"fjkhf"])
print(type(KKK))
print(KKK)

#accesing Set

for element in KKK:
  print(element)                                 #cannot fetch individual element because unordered and unique
 
#Method Set  

K = {23,43,3,4,6,"fhfh",True,False,-45}

K.add("kky")                         #add one element in the set
print(K)
K.update([23,488,True])              #add multiple elements in the set
print(K)
K.remove("fhfh")                     #remove particular element from the set if not found throw error
#K.remove("TGGTH")
print(K)
K.discard(True)                      #remove particular element from set and not throw error if not found 
K.discard("not exist")
print(K)
K.pop()                              #delete the left side element in unordered set 
print(K.pop())
print(K)
K.clear()                           #delete all elements from the set
print(K) 


# Set Operation

S1 = {23,45,43,56,3,2,35,34}
S2 = {45,56,54,5,456,544,56,23,98}
S3 = {54,65,45,6,4,3}

union = S1 | S2 | S3
print(union)                       #union operation in set

intersection = S1 & S2
print(intersection)                #intersection operation in set

difference = S1 - S2
print(difference)                  # difference operation in set

symmetricDifference = S1 ^ S2
print(symmetricDifference)         # symmetric difference in set(opposit output than intersection)


                                   #Exercise

# Write a program  to create a dictionary of Hindi words with values as their english translation.Provide user with an option to look it up

hindi_english_dict = {
    "नमस्ते": "Hello",
    "आप": "You",
    "कैसे": "How",
    # Add more words and translations as needed
}

word = input("Enter the word :")
try:
  print(hindi_english_dict.get(word))
except ValueError as e:
  print(e)    

# Write a program to input eight numbers from the user and display all the unique numbers(once)

S1 = set()
for element in range(8):
  x = int(input("Enter the element:"))
  S1.add(x)
print(S1)  
print(type(S1)) 

#Can we have a set with 18(int) and "18"(str) as a values in it

S1 = {18,"18",33,"33"}
print(S1)                                     #Output -> {'33', 33, 18, '18'}
print(type(S1))    

# What will be the length of following set
S = set()
S.add(20)
S.add(20.0)
S.add("20")
print(S)
print(len(S))                       # output -> 2  

# Check the type of S

S = {}
print(type(S))                      #Output -> <class 'dict'>  

# Create an empty dictionary. Allow 4 friend to enter their favourite language as values and use keys as their names. Assume that the names are unique

E = {}

for element in range(4):
  key = input("Enter your name :")
  value = input("Enter your favourite subject :")
  E.update({key : value})
print(E)                   

# If the name of two friends are same in above program than what will to program
  # ans -> the latest value of the key will replace to old one if there is same key value assign


#If the language of two friends are same in above program than what will to program
  # Ans -> value can be same in dictionary but key should unique so there is no problem program will work smoothly with same values

#Can you change the values of the values inside a list which is containes in set

S = {8,7,12,"Harry",[1,2]}
S = {8, 7, 12, "Harry", (1, 2)}
my_list = [1, 2]
S.remove(my_list)

my_list[0] = 100
my_list[1] = 200

S.add(tuple(my_list))

print(S)                 # output -> Error ! Because list not allow in set but tuple allow
