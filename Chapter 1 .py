#Write a program to print Gayatri mantra using python

print("ॐ भूर्भुव॒ स्सुवः॑ \nतत्स॑ वि॒तुर्वरे᳚ण्यं॒ \nभर्गो॑ दे॒वस्य॑ धीमहि \nधियो॒ यो नः॑ प्रचो॒दया᳚त् ॥")

#write a program to print content of a file using os module

import os 
with open("p1.py","r") as file:
  content= file.read()
print(content)

import datetime
currentTime =datetime.datetime.now()
print(currentTime)

#Write a program to use external module

import numpy as np

data = [1, 2, 3, 4, 5]
mean = np.mean(data)
print("The mean of the data is:", mean)

