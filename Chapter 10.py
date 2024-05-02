"""class Animal:
  def __init__(self):
    pass
  
class pet(Animal):
  def __init__(self):
    pass 
  
class dog(pet):
  def sound(self):
    print("Bark")

dogSound = dog()
dogSound.sound()    

#2

class Employee:
    def __init__(self, salary, increment):
        self._salary = salary
        self._increment = increment

    @property
    def salary(self):
        return self._salary

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, new_increment):
        if new_increment < 0:
            raise ValueError("Increment value must be non-negative")
        self._increment = new_increment

    @property
    def salaryAfterIncrement(self):
        return self.salary * (1 + self.increment / 100)

# Example usage:
emp = Employee(50000, 5)  # Create an Employee instance with initial salary and increment
print("Initial Salary:", emp.salary)
print("Initial Increment:", emp.increment)
print("Salary After Increment:", emp.salaryAfterIncrement)

# Change the increment value
emp.increment = 10
print("\nUpdated Increment:", emp.increment)
print("Salary After Increment with updated increment:", emp.salaryAfterIncrement) 

A = [2,6,3,6,23,32,56,98]
for index,value in enumerate(A):
  if index == 2 or index == 4 or index == 6:
    print(value)"""

a = int(input("Enter the integer : "))
b = int(input("Enter the integer : "))

try:
  print(a/b)
except ValueError as v:
  print(v)  




