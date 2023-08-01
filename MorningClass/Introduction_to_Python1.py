from abc import ABC, abstractclassmethod
from tkinter import messagebox
import math
import tkinter as tk
# Running python scripts


# print('Martha')
# print("I love python")

# #PEP8: PythonScript guidelines
# #Indentation

# #snake_case commonly used in Python
# #PascalCase the first letter is capitalized

# #COMMENTS
# #single line comment

# """
# Multiline comment
# """


# #variables in python
# name = "Martha Namugga"
# age = 20
# print(name)
# print(age)
# print("my name is " + name + " my age is " +str(age))


# #DATA STRUCTURES(datatypes)
# """
# numeric values are numbers from 1- 10
# Integer vales are for whole numbers
# Floating point values are decimal numbers eg pi = 3.14

# string values are str
# 'martha' or "Namugga"
# numbers in form of string "10" or '2'

# Boolean values are logical values
# True or False

# Sequence types
# list - enclose with square brackets. represented in an ordered manner[]
# tuple - enclose with parentheses()
# range - use iteration or apply loops
# set - enclose with curly brackets.unordered collection type,unique


# Mapping types
# dict - enclose with curly braces{}

# {
#     name: "Martha",
#     age: 20
# }
# or
# {name: "Martha", age: 20}

# item Dict
# {Apple, banana, orange
# }

# None Types: None
# represents absence of a value
# name: none

# """
# gen_gender = True
# print(gen_gender)


# ----------------------------------------------------------------


#                           DAY 2
""" 
  CONTROL FLOW
 1. conditional statements (if elif else)
flow conditions show what to do when faced with a certain condition


if condition1:
    print("condition1 is true") # prints when thr first condition is tru

elif condition2:
    print("condition2 is true") # prints when the first is false but second true
 
else:
    print("no condition is true") # prints when none of the conditions ar true
"""

# #Example and exercise

# age = 79
# if age < 18:
#     print("You are underage")
# elif age >= 18 and age <= 65:
#     print("You are an adult")
# else:
#     print("You are a senior citizen")


# #2 LOOPS (For, while)
# """
# #help you iterate over a sequence

# for i in sequence:
#     print(i)
# """
# #examples and exercise of for
# cars = ["tesla", "volvo","Ford", "BMW","Toyota"]
# for car in cars:
#     print(car)
# fruits = ["apple","orange","banana","mango"]
# for fruit in fruits:
#     print(fruit)
# for fruit in range (1,3):
#     print(fruit)


# """
# #while loop helps execute as long as condition is true
# """
# #examples of while
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# fruits = ["apple","orange","banana","mango"]
# fruitcount =0
# while fruitcount < len(fruits):
#     print(fruits[fruitcount])
#     fruitcount += 1


# """
# #Break and Continue statements
# Break terminates a statment
# """
# #examples and exercise
# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)
# #continue
# for x in range(1,10):
#     if x == 5:
#          continue
#     print(x)

# fruits = ["apple","orange","banana","mango"]
# for fruit in fruits:
#     if fruit == "banana":
#         break
#     print(fruit)
#     if fruit == "orange":
#         continue
#     print(fruit)


# #EXCEPTION HANDLING (Try, exept finally)
# """
# try block is used to monitor a code which we think will throw an error
# we catch these excpetations
# except block is used to handle exceptions
# finally block runs regarless

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("error!! cannot divide by zero")
# finally:
#     print("This block will run regardless") #complete execution
# """

# try:
#     numbers = [1, 2, 3, 4, 5]
#     index = int(input("Enter an index: "))
#     value = numbers[index]
#     print("Value at index", index, "is", value)

# except IndexError:
#     print("Error: Index out of range.")

# finally:
#     print("Finally block always executed")


# #EXAMPLES
# #Using the emotion example using DICT
# """"""
# emotions = {
#     "happy": "I'm glad to hear you are happy",
#     "sad": "I sorry to hear that you're feeling sad",
#     "angry": "Take a deep breath and try to stay alive.",
#     "fearful": "I understand that fear can be challenging",
#     "disgusted": "It's unfortunate that you're feeling disgusted",
# }
# #prompt the user to enter their emotions
# user_emotion =input("How are you feeling today? ")
# #convert the user_emotion in lowercase to lowercase
# user_emotion = user_emotion.lower()
# #check if the user_emotion is in the emotions dict
# if user_emotion in emotions:
#     print(emotions[user_emotion])

# else:
#     print("I don't understand your emotion")


# #Write a program to ask a student about their mental health

# name  = input("What is your name? ")
# name = name.lower
# rate = input("on a scale of 1 to 10. Rate your mental health ")
# rate = int(rate)


# if rate < 3:
#     print( " Please see a doctor")
# elif rate >=3 and rate <= 8:
#     print(" You are good to go. Just rest some more")
# else:
#     print("You are excellent")


# ----------------------------------------------------------------
#                             DAY 3


# Basic operators and expressions (input and output operators)

"""
Arithmetic operators
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
// Divide return the quotient without the remainder
** Exponentiation

Comparison Operators
< Less than
> Greater than
<= Less than or equal to
>= Greater than or equal to
== Equal to
!= Not equal to

Logical operators
logical AND 'and' 
logical OR 'or'
logical NOT 'not'

Assignment Operators
Assign values: "="
Add value: "+"
add and assign: "+="
subrtract and assign: "-="
multiply and assign: "*="
divide and assign: "/="
modulus and assign: "%="

Membership Operators
In: 'in' it checks if a value exists 
not in: 'not in' it checks if a value does not exist

Identity Operators:
is: 'is'  checks if two values are the same
is not: 'is not' checks if two values are not the same
"""

# EXAMPLES OF ARITHMETIC OPERATORS
# #addition
# x = 50 + 45
# print(x)
# # - Subtraction
# y = 50 - 45
# print(y)
# # * Multiplication
# z = 10 * 2
# print(z)
# # / Division
# a = 50 / 5
# print(a)
# # % Modulus
# b = 10 % 3
# print(b)
# # // Divide return the quotient without the remainder
# c = 50 // 45
# print(c)
# # ** Exponentiation
# d = 2 ** 5
# print(d)

# #EXAMPLES OF COMPARISON OPERATORS:
# a = 29
# b = 60
# #greater than
# if a > b:
#     print ("a is greater than b")
#     print(a>b)
#  #less than
# if a < b:
#     print ("a is less than b")
#     print(a<b)
# #equal to
# if a == b:
#     print ("a is equal to b")
#     print(a==b)
#  #not equal to
# if a != b:
#     print ("a is not equal to b")
#     print(a!=b)
# #greater than or equal to
# print(a <= b)
# #less than or equal to
# print(a >= b)
# #equal to
# print(a == b)

# #EXAMPLES OF LOGICAL OPERATORS
# a = True
# b = False
# print(a and b) #logical and
# print(a or b) #logical or
# print(not a ) #logical not
# print(not b)

# #EXAMPLES OF ASSIGNMENT OPERATORS
# #compound assignment operators
# a = 10

# # add and assign: "+="
# a += 5
# print(a)
# # subrtract and assign: "-="
# a -= 5  # the new value of a is got from the answer above
# print(a)
# # multiply and assign: "*="
# a *= 5
# print(a)
# # divide and assign: "/="
# a /= 5
# print(a)
# # modulus and assign: "%="
# a %= 5
# print(a)


# #EXAMPLES OF MEMBERSHIP OPERATORS
# cars = ["jeep", "tesla", "BMW",]
# print("jeep" in cars)
# print("tesla" in cars)
# print("toyota" in cars)
# print("volvo" not in cars)

# #EXAMPLES OF IDENTITY OPERATORS

# x = 10
# y = 10
# z =[1,2,3,4,5,6,7,8,9]
# w = [1,2,3,4,5,6,7,8,9]

# #is operators
# print(x is y)
# print(x is not y)

# print(z is w)
# print(z is not w)

# EXAMPLES OF BITWISE OPERATORS
""" 
bitwise operator are used to perform operations on individual  bits 
of binary numbers

bitwise AND ('&'): performs a bitwise and operation between two corresponding bits of two integers
bitwise OR ('|'): performs a bitwise or operation between two corresponding bits of two integers
bitwise XOR ('^'): performs a bitwise XOR operation between two corresponding bits of two integers
bitwise NOT ('~'): performs a bitwise NOT operation between two corresponding bits of (flips numbers)
Bitwise left shift('<<'): performs a bitwise left shift. so shifts bits to the left
Bitwise right shift('>>'): performs a bitwise right shift. so shifts bits to the right
"""

# a = 10 #1010 in binary
# b = 20 #10100

# #bitwise AND operation
# result_and = a & b
# print(result_and)

# #bitwise OR operation
# result_or = a | b
# print(result_or)

# #bitwise XOR operation
# result_xor = a ^ b
# print(result_xor)

# #bitwise NOT operation
# result_not = ~a
# print(result_not)

# #bitwise left shift operation
# result_left_shift = a << 2
# print(result_left_shift)

# #bitwise right shift operation
# result_right_shift = a >> 2
# print(result_right_shift)


# #EXAMPLE AND ASSIGNMENT
# #Create a simple calculator function to calculate (add, subtract, multiply, divide)

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

# def main():
#     a = float(input("Enter the first number: "))
#     b = float(input("Enter the second number: "))

#     operator = input("Enter the operator (+, -, *, /): ")

#     if operator == "+":
#         result = add(a, b)
#     elif operator == "-":
#         result = subtract(a, b)
#     elif operator == "*":
#         result = multiply(a, b)
#     elif operator == "/":
#         result = divide(a, b)
#     else:
#         print("Invalid operator")

#     print("the result is : ", result)

# if __name__ == "__main__":
#     main()


# tkinter learn       #EXERCISE ON CALCUATOR WITH GUI
"""create a simple calculator program with a GUI. 
make the title of the calculator program window with your name
eg Martha simple calculator
"""

# from tkinter import *
# def onClickBtn(number):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, current + str(number))

# def btndot():
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, current + ".")

# def btnclear():
#     entry.delete(0, tk.END)


# def btnequal():
#     expression = entry.get()
#     try:
#         result = eval(expression)
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, result)
#     except Exception:
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, "Error")

# # Create the main root
# root = tk.Tk()
# root.title("Martha's Calculator")
# root.configure (bg="#17161b")


# # Creating thw result field
# entry = tk.Entry(root, bg="#17161b", fg="white", font=("Courier", 20))
# entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# # Create buttons for numbers and operators
# btn1 = tk.Button(root, text="1", padx=20, pady=10,fg="#fff", bg="#2a2d36", command=lambda: onClickBtn(1))
# btn2 = tk.Button(root, text="2", padx=20, pady=10,fg="#fff", bg="#2a2d36", command=lambda: onClickBtn(2))
# btn3 = tk.Button(root, text="3", padx=20, pady=10,fg="#fff", bg="#2a2d36", command=lambda: onClickBtn(3))
# btn4 = tk.Button(root, text="4", padx=20, pady=10,fg="#fff", bg="#2a2d36", command=lambda: onClickBtn(4))
# btn5 = tk.Button(root, text="5", padx=20, pady=10,fg="#fff", bg="#2a2d36", command=lambda: onClickBtn(5))
# btn6 = tk.Button(root, text="6", padx=20, pady=10,fg="#fff", bg="#2a2d36", command=lambda: onClickBtn(6))
# btn7 = tk.Button(root, text="7", padx=20, pady=10,fg="#fff",bg="#2a2d36",command=lambda: onClickBtn(7))
# btn8 = tk.Button(root, text="8", padx=20, pady=10,fg="#fff",bg="#2a2d36", command=lambda: onClickBtn(8))
# btn9 = tk.Button(root, text="9", padx=20, pady=10,fg="#fff", bg="#2a2d36",command=lambda: onClickBtn(9))
# btn0 = tk.Button(root, text="0", padx=20, pady=10,fg="#fff", bg="#2a2d36",command=lambda: onClickBtn(0))

# btnadd = tk.Button(root, text="+", padx=20, pady=10, fg="#fff",bg="#3697f5", command=lambda: onClickBtn("+"))
# btnsubtract = tk.Button(root, text="-", padx=20, pady=10,fg="#fff",bg="#3697f5", command=lambda: onClickBtn("-"))
# btnmultiply = tk.Button(root, text="*", padx=20, pady=10,fg="#fff",bg="#3697f5", command=lambda: onClickBtn("*"))
# btndivide = tk.Button(root, text="/", padx=20, pady=10,fg="#fff",bg="#3697f5", command=lambda: onClickBtn("/"))
# btnclear = tk.Button(root, text="C", padx=20, pady=10,fg="#fff",bg="#3697f5", command=btnclear)
# btnequal = tk.Button(root, text="=", padx=20, pady=10,fg="#fff",bg="#3697f5", command=btnequal)

# # Position the buttons on the grid
# btn1.grid(row=3, column=0)
# btn2.grid(row=3, column=1)
# btn3.grid(row=3, column=2)

# btn4.grid(row=2, column=0)
# btn5.grid(row=2, column=1)
# btn6.grid(row=2, column=2)

# btn7.grid(row=1, column=0)
# btn8.grid(row=1, column=1)
# btn9.grid(row=1, column=2)

# btn0.grid(row=4, column=1)

# btnadd.grid(row=1, column=3)
# btnsubtract.grid(row=2, column=3)
# btnmultiply.grid(row=3, column=3)
# btndivide.grid(row=4, column=3)
# btnclear.grid(row=4, column=0)
# btnequal.grid(row=4, column=2)

# # Start the main event loop
# root.mainloop()


# ----------------------------------------------------------------

#                            DAY 4

#   OBJECT - ORIENTED PROGRAMMING(00P)
"""
   Key concepts are;
1. Class
2.Object
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Abstraction
"""

""" 1. CLASS

A class is a blueprint for creating objects.
"""

# # Example 1: Car
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def start_engine(self):
#         print("Starting the engine")

#     def stop_engine(self):
#         print("Stopping the engine")

# my_car = Car("Toyota", "Corolla", "2022")
# print(my_car.make)
# print(my_car.model)
# print(my_car.year)
# my_car.start_engine()
# my_car.stop_engine()

# #Example 2. Bank Account
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if self.balance >= amount :
#           self.balance -= amount
#         else :
#             print("Insufficient funds")

#     def display_balance(self):
#         print("Account number: " + str(self.account_number))
#         print("Balance: ",self.balance)

# #create bank object
# my_bank = BankAccount(1234, 10000)

# #operations
# my_bank.display_balance()
# my_bank.deposit(5000)
# my_bank.display_balance()
# my_bank.withdraw(17000)
# my_bank.display_balance()

# #Example 3. Rectangle

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# #creating an object
# my_rectangle = Rectangle(10, 5)
# #calculate and display area and perimeter
# print(my_rectangle.area())
# print(my_rectangle.perimeter())


# #Example 3. Student

# class Student:
#     def __init__(self, name, year, course):
#         self.name = name
#         self.year = year
#         self.course = course

#     def display_details(self):
#         print("Name: ", self.name)
#         print("Year: ", self.year)
#         print("Course: ", self.course)

# # creating an object
# my_student = Student("Martha",  3, "BSSE")
# my_student.display_details()


# 2.  OBJECT
"""
An object is an instance of a class.
"""

# # Example 1: Person
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greeting(self):
#         print("Hello " , self.name)
#         print("I am " + str(self.age) + " years old")

# #create a person object
# my_person1 = Person("Martha", 3)
# my_person2 = Person("Hellen", 44)
# print(my_person1.name)
# my_person1.greeting()
# my_person2.greeting()


# # Exercise 1: claculate the area and circumference of a circle

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

#     def circumference(self):
#         return 2 * 3.14 * self.radius

# my_circle = Circle(radius=7)
# print(my_circle.area())
# print(my_circle.circumference())

# # exercise 2:
# # calculate and display employees(0.5 of salary) bonuses
# # employee 1 salary = 150000
# # employee 2 salary = 230000

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         self.bonus = 0.5 * self.salary

#     def display_details(self):
#         print("Name: ", self.name)
#         print("Salary: ", self.salary)
#         print("Bonus: ", self.bonus)

# #creating objects
# my_employee1 = Employee("Martha", 150000)
# my_employee2 = Employee("Hellen", 230000)

# my_employee1.display_details()
# my_employee2.display_details()


# 3. ENCAPSULATION
"""
Goals of encapsulation are;
1. Data hiding
2. protect objects from changes
3. protect objects from external changes
4. code organization and modularity
"""

# # Example: with bank accounts
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self._account_number = account_number # encapsulates the account number attribute
#         self._balance = balance # encupsuates the balance attribute

#     def deposit(self, amount):
#         self._balance += amount

#     def withdraw(self, amount):
#         if self._balance >= amount :
#             self._balance -= amount
#         else :
#             print("Insufficient funds")

#     def get_balance(self):
#         return self._balance

# #create new object
# my_bank = BankAccount(1234, 10000)
# #access the bank object and modify its properties
# print(my_bank.get_balance())
# my_bank.deposit(5000)
# print(my_bank.get_balance())
# my_bank.withdraw(12000)
# print(my_bank.get_balance())

# #Exercise 2. Convert temperature from celsius to fahrenheit

# class Temperature:
#     def __init__(self, celsius):
#         self._celsius = celsius
#         self._fahrenheit = (celsius * 9 / 5) + 32

#     def get_fahrenheit(self):
#         return self._fahrenheit

# #creating an object
# my_temperature = Temperature(30)
# print(my_temperature.get_fahrenheit())


# ASSIGNMENT 1. Show encapsulation with employee informatiom to give a pay incrementatiom
# #Salary with employee informatiom to new_salary eg from 850000 to 1000000

# class Employee:
#     def __init__(self, name, salary):
#         self._name = name
#         self._salary = salary

#     def new_salary(self):
#         new_salary = self._salary + (self._salary * 0.1)
#         return new_salary

#     def display_details(self):
#         print("Name: ", self._name)
#         print("Salary: ", self._salary)
#         print("New Salary: ", self.new_salary())

# #creating an object
# my_employee = Employee("Martha", 850000)
# my_employee.new_salary()
# my_employee.display_details()


# ----------------------------------------------------------------
# DAY 5 (WEEK TWO FRIDAY)


# INHERITANCE
"""
Inheritance is a mechanism that allows a class to inherit the properties and methods of another class.
syntax
class Employee(Person)
"""


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating ...")


# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} is barking...Woof")


# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} is meowing...")


# # creating objects
# animal = Animal("Generic Animal")
# my_dog = Dog("Snoopy")
# my_cat = Cat("Fluffy")

# invoking methods
# animal.eat()
# my_dog.bark()
# my_dog.eat()
# my_cat.meow()
# my_cat.eat()

# Example 2. Demonstrating Inheritance


# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def display_details(self):
#         print(f"Brand: {self.brand}")
#         print(f"Color: {self.color}")

#     def drive(self):
#         print("Moving the vehicle")


# class Car(Vehicle):
#     def __init__(self, brand, color, wheels):
#         super().__init__(brand, color)
#         self.wheels = wheels

#     def display_details(self):
#         super().display_details()
#         print(f"Wheels: {self.wheels}")

#     def honk(self):
#         print("Beep Beep")

# #Creating car object
# my_car = Car("Ford", "Blue", 4)

# #modify the car object
# print(f"Brand is: {my_car.brand}")
# my_car.color = "black"

# #invoke car methods
# my_car.display_details()
# my_car.drive()
# my_car.honk()


# Exercise 1
# Demonstrate using inheritance to calculate are, perimeter of a circle and rectangle
# Generate a base class of shape

# #imported math module
# class Shape:
#     def area(self):
#         pass

#     def perimeter(self):
#         pass


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius**2

#     def perimeter(self):
#         return 2 * math.pi * self.radius


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)


# # Creating a Circle object and calculating its area and perimeter
# circle = Circle(5)
# circle_area = circle.area()
# circle_perimeter = circle.perimeter()
# print(f"Circle Area: {circle_area:.2f}")
# print(f"Circle Perimeter: {circle_perimeter:.2f}")

# # Creating a Rectangle object and calculating its area and perimeter
# rectangle = Rectangle(4, 6)
# rectangle_area = rectangle.area()
# rectangle_perimeter = rectangle.perimeter()
# print(f"Rectangle Area: {rectangle_area}")
# print(f"Rectangle Perimeter: {rectangle_perimeter}")


# #Example 3.
# #Multiple Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating ...")

# class Flyable:
#     def fly(self):
#         print(f"{self.name} is flying ...")

# class Bird(Animal, Flyable):
#     def __init__(self, name, species):
#         super().__init__(name)
#         self.species = species

#     def display_details(self):
#         print(f"Name: {self.name}")
#         print(f"Species: {self.species}")

# #creating bird objects and invoking methods
# my_bird = Bird("Pigeon", "bird")
# my_bird.eat()
# my_bird.fly()
# my_bird.display_details()


# METHOD OVERRIDING
"""
Method overriding is a mechanism that allows a class to change the properties and methods of another class.

"""

# class Animal:
#     def make_sound(self):
#         print(f"Animal is making a sound ...")

# class Dog(Animal):
#     def make_sound(self):
#         print(f"Dog is barking ...")

# class Cat(Animal):
#     def make_sound(self):
#         print(f"Cat is meowing ...")

# def make_animal_sound(animal):
#     animal.make_sound()

# #creating objects
# animal = Animal()
# dog = Dog()
# cat = Cat()

# #calling make_animal_sound function (uses the objects we created above)
# make_animal_sound(animal)
# make_animal_sound(dog)
# make_animal_sound(cat)


# POLYMORPHISM
"""
Polymorphism is a mechanism that allows a class to have multiple forms.
Code that can work with different objects

Method overriding and method overloading
overriding occurs when the sub class provides its own implementation of a method
Overloading allows a class to have multiple methods with the same name but diifernt parameters or implementation
"""

# Example of polymorphism


# class shape:
#     def area(self):
#         pass


# class Rectangle(shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# class Circle(shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius**2

#     def circumference(self):
#         return 2 * 3.14 * self.radius


# # creating shape objects and displayong area
# rectangle = Rectangle(4, 6)
# circle = Circle(5)
# print(f"area of rectangle: {rectangle.area()}")
# print(f"area: {circle.area()}")
# print(f"circumference: {circle.circumference()}")


# OVERLOADING
# class calculator:
#     def add(self, x, y):
#         return x + y
#     def add(self, x, y,z):
#         return x + y + z

# #create object
# calc = calculator()
# # print(calc.add(1, 2))
# print(calc.add(1, 2, 3))


# ABSTRACTION
"""
Abstraction allwows focus on essential features and hide them from unncessary details
"""

# Exmample 5. Demonstraition of Abstraction

# class Vehicle(ABC):
#     @abstractclassmethod
#     def start(self):
#         pass
#     @abstractclassmethod
#     def stop(self):
#         pass

#     @abstractclassmethod
#     def drive(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         print("Starting the car")

#     def stop(self):
#         print("Stopping the car")

#     def drive(self):
#         print("Driving the car")

# class Truck(Vehicle):
#     def start(self):
#         print("Starting the truck")

#     def stop(self):
#         print("Stopping the truck")

#     def drive(self):
#         print("Driving the truck")

# #creating objects
# car = Car()
# truck = Truck()

# #invoking methods
# car.start()
# car.stop()
# car.drive()
# truck.start()
# truck.stop()
# truck.drive()

# demonstrate abraction using calculating area of a circle and rectangle

# class Shape:
#     @abstractclassmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius**2

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return  self.length * self.width

# #creating objects
# circle = Circle(5)
# rectangle = Rectangle(4, 6)

# #invoking methods
# print(circle.area())
# print(rectangle.area())


# ASSIGNMENT 1.
# CREATE A RECEIPT PRINTING PRIGRAM WITH GUI INTERFACE
# more advanced detail earns more points


class ReceiptGenerator:
    def __init__(self, window):
        self.window = window
        self.window.title("Martha's Receipt Generator")
        window.configure(bg="#17161b")

        self.item_name = tk.StringVar()
        self.item_quantity = tk.IntVar()
        self.item_price = tk.DoubleVar()

        self.item_name_label = tk.Label(
            window, text="Item Name:", bg="#17161b", fg="white", font=("Courier", 20))
        self.item_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.item_name_entry = tk.Entry(window, textvariable=self.item_name)
        self.item_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.item_quantity_label = tk.Label(
            window, text="Quantity:", bg="#17161b", fg="white", font=("Courier", 20))
        self.item_quantity_label.grid(row=1, column=0, padx=10, pady=10)
        self.item_quantity_entry = tk.Entry(
            window, textvariable=self.item_quantity)
        self.item_quantity_entry.grid(row=1, column=1, padx=10, pady=10)

        self.item_price_label = tk.Label(
            window, text="Price:", bg="#17161b", fg="white", font=("Courier", 20))
        self.item_price_label.grid(row=2, column=0, padx=10, pady=10)
        self.item_price_entry = tk.Entry(window, textvariable=self.item_price)
        self.item_price_entry.grid(row=2, column=1, padx=10, pady=10)

        self.add_button = tk.Button(
            window, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.receipt_text = tk.Text(window, height=10, width=30)
        self.receipt_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.total_label = tk.Label(window, text="Total:")
        self.total_label.grid(row=5, column=0, padx=10, pady=10)
        self.total_value = tk.Label(window, text="")
        self.total_value.grid(row=5, column=1, padx=10, pady=10)

        self.items = []

    def add_item(self):
        name = self.item_name.get()
        quantity = self.item_quantity.get()
        price = self.item_price.get()

        if name and quantity and price:
            item_total = quantity * price
            self.items.append((name, quantity, price, item_total))
            self.update_receipt()
            self.clear_inputs()
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")

    def update_receipt(self):
        self.receipt_text.delete("1.0", tk.END)

        total = 0

        for item in self.items:
            name, quantity, price, item_total = item
            self.receipt_text.insert(
                tk.END, f"{name} -> {quantity} = UGX {item_total:.2f}\n")
            total += item_total

        self.total_value.config(text=f"UGX {total:.2f}")

    def clear_inputs(self):
        self.item_name.set("")
        self.item_quantity.set(0)
        self.item_price.set(0.0)


window = tk.Tk()
receipt_generator = ReceiptGenerator(window)
window.mainloop()
