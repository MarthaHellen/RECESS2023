# Floats, strings, int, lists, dictionaries, char, booleans
# variables store data that is of different type

# LISTS, TOOPLES, DICTIONARIES, SETS

# w = 'sorry'
# z = 77
# y = 1j
# print(type(w))
# print(type(z))
# print(type(y))

# #1. LISTS
# """
# lists are used to store in a single variable
# inbuilt datatype
# use square brackets
# they are ordered and can be changed
# allows duplicated values
# """
# students = ["Martha","zahara","Trisha"]
# Students = ["Martha","zahara","Trisha", "Martha", "Zahara"] #duplicate
# print(students)
# print(Students)

# #operations on lists
# print(len(Students))
# print(Students[0])
# print(Students[-3])
# Students[1]= "Namugga"
# print(Students)
# Students.append("Hellen") #adding items at the end
# print(Students)
# Students.insert(1,"luyombo") #adding items at a specified position
# print(Students)
# Students.remove("Trisha")
# print(Students)
# Students.pop(0)
# print(Students)
# print(type(Students))
# # print(Students[1:3]) #This line retrieves elements from index 1 to index 2 (exclusive)
# # print(Students[:3]) #Here, the slice starts from the beginning of the list and goes up to index 2
# # print(Students[3:]) #starts from index 3 and goes until the end of the list
# # print(Students[:]) #[:] retrieves all elements in the list, effectively creating a copy of the original list.
# # print(Students[::2]) #The step value 2 skips every second element. It starts from the beginning
# # print(Students[::-1]) #The negative step value -1 reverses the list, so all elements are returned in reverse order.
# # print(Students[::-2]) #negative step value -2 selects every second element in reverse order. It starts from the end of the list


# #2. TUPLES
# """
# Store items in a single variable
# yuples are ordered and unchangable
# uses ()
# """
# phones = ("samsung", "iPhone", "Techno", "samsung", "iPhone")
# print(phones)

# #using for loops
# for x in phones:
#     print(x)

# #operations in a tuple
# Tuple1 =("rice", "meat")
# Tuple2= (100, 400, 600)
# print(Tuple1)
# # print(type(Tuple1))

# #exercise how to access turples and indexing and length
# print(Tuple1[0])
# print(len(Tuple1))

# #adding the items in a tuple(change it to a list 1st)
# z = list(phones)
# z.append("Nokia")
# phones = tuple(z)
# print(phones)

# # adding two tuples
# laptops = ("Dell","HP","Acer")
# laptop = ("samsung",)
# laptops += laptop
# Newstock = laptops + laptop
# print(Newstock)
# print(laptops)


# #3. SETS
"""
store multiple items in a single variable
unchangeable but can remove and add some variables
unordered and dont allow duplicates
{}
"""
""" 
set1 = {"rice", "meat","beans","peas"}
print(set1)

#exercise find length, data type, accessing items, add items, add two sets
print(len(set1))
print(type(set1))
set1.add("yams")
print(set1)

set2 = "eggplant"
print(set1.union(set2))

for i in set1:
    print(i)
"""

# ----------------------------------------------------------------


# DAY 2
""" 
#DICTIONARIES
Used to store values in key:value pairs
they are ordered and changeable but dont allow duplicate
can have data of different types
"""
# Examples
"""
myDict = {
    "name": "Martha",
    "age": 99,
    "gender": "female"
}

print(myDict)
#length of dictionary
print(len(myDict))
print(type(myDict))

#Access to dictionary
print(myDict["name"])
print(myDict.get("gender"))
print(myDict.values())
print(myDict.keys())
"""
"""EXERCISES ON DICTIONARY
return all the values
check if a key exits in the dictionary
changing dictionary items
updating dictionary items
how to add dictionary items
how to remove dictionary items
loop through a dictionary 


<<<<< see below>>>>>
"""
"""
#updating an item in the dictionary
myDict["gender"] = "male"
print(myDict)

#Adding an item in the dictionary
myDict["height"] = 180
print(myDict)

#Deleting an item in the dictionary
del myDict["name"]
print(myDict)

#checking if key is in the dictionary
if "name" in myDict:
    print("name is in the dictionary")
else:
    print("name is not in the dictionary")

# Looping through the dictionary
for key, value in myDict.items():
    print(key, ":", value)
"""


################################################################

# NUMBERS
# integers, floats, complex numbers
# w = 10 #int
# r = 10.5 #float
# s = 44j #complex number
""" 
print(type(w))
print(type(r))
print(type(s))

#integers
a = 2
b = 27794766737
c = -54674894038
print(type(a))
print(type(b)))
print(type(c))

#floats
h = 2.9
g = 27.794766737
f = -54.674894038
print(type(h))
print(type(g))
print(type(f))

#complex numbers
a = 10 + 2j
b = 27794766737j
c = -5j
print(type(a))
print(type(b))
print(type(c))


#type conversions
w = 10 #int
r = 10.5 #float
s = 5 + 3j #complex number

#Exercises on conversions

print(int(r)) #change float  to int
print(complex(r)) #change float to complex number
print(complex(w)) #change int to complex number
# print(int(s))
# print(float(s))
"""

################################

# CASTING
"""
works mostly when we want to specify cariable type
"""

# x= int(20)
# y = int(300000)
# z = int("8") # a is 8

# print(x)
# print(y)
# print(z)

################################################################


# #STRINGS
# print ("Afternoon")
# print ('Evening')

# #Assign string to variable
# w = "Afternoon"
# print(w)

# #Multiline string
# q="""
# I am offering BSSE
# year three
# Currently doing recess in python, data science and Django
# """
# print(q)

# #Strings as arrays
# a = "Afternoon"
# print(a[1])

"""
Exercises on Strings
1.use len() to determine the length of string
2.loop through strings
3. slicing the string
4. concatenating
5.

<<<see below>>>
"""
# greet = " Hello, Welcome  "
# print(len(greet))

# for x in range(len(greet)) :
#     print(greet[x])


# #How to modify strings
# print(greet.lower())
# print(greet.upper())

# #Remove whitespace
# print(greet.strip())
# print(greet.lstrip())
# print(greet.rstrip())

# #String concatenation
# a = "good "
# b = "morning"
# print(a+b)

# Format string
# age = 23
# name = "My name is martha and i am " + str(age)

""" 
#using the format method
the formart() function takes the passed parameters, formarts them
and places them into where the place holders are
"""
# name = "My name is martha and i am {} "
# print(name.format(age))

################################################################

# BOOLEAN
# These evaluate to true or false
# print(20<50)
# print(20>50)
# print(20==20)

# print(bool(15))
# r = "Martha"
# print(bool(r))

# Exercises
# use a condition to show the use of boolean values
# if (20>50):
#     print("True")
# else:
#     print("False")


# ----------------------------------------------------------------
from math import *
 # DAY 3


# #         INDIVIDUAL ASSIGNMENT
# # EXERCISE 1 (LISTS)
# name = ["Martha","Hellen", "Marian","Hope","Zahara"]

# #1. output 2nd item
# print(name[1])
# #2. change value of 1st item
# name[0] = "Trisha"
# print(name)
# #3. add 6th item
# name.append("Sarah")
# print(name)
# #4. add bethel as 3rd item in list
# name.insert(2,"Bethel")
# print(name)
# #5. remove 4th item
# name.remove(name[3])  #use pop also
# print(name)
# #6. using negative indexing to print last element
# print(name[-1])
# #7.new list and use range of index to print
# fruits =["apple", "orange","banana","pears","pineapple","avocado","grape"]
# print(fruits[0:6])
# #8. list of countries and make a copy of it
# countries = ["India","USA","Canada","Australia","New Zealand"]
# countries_copy = countries.copy()
# print(countries_copy)
# #9. loop through countries
# for country in countries:
#     print(country)
# #10. list of animals and sort in acsending and descending order
# animals = ["dog","cat","bird","fish","horse","cow","antelope"]
# animals.sort()
# print(animals)
# animals.sort(reverse=True)
# print(animals)
# #.11 output any animal with a
# for animal in animals:
#     if animal.startswith("a"):
#         print(animal)
# #(when a is anywhere in animal)
# if 'a' in animals:
#     print(animal)

# #12. joining two lists
# firstName = ["Martha","Hellen","Hope"]
# secondName = ["Namugga", "Namiira","Agaba"]
# print(firstName + secondName)


# # EXERCISE 2 (TUPLES)

# x = ("samsung","iphone","techo","redmi")
# print(x)
# #1. ouput favorite phone brand
# print(x[1])

# #2.negative indexing print second last
# print(x[-2])

# #3. update iphone to itel
# z = list(x)
# z[1] = "itel"
# x = tuple(z)
# print(x)

# #4. add Huawei to tuple
# y = list(x)
# y.append("Huawei")
# x = tuple(y)
# print(x)

# #5. loop through tuple
# for x in x:
#     print(x)

# #6. remove first item from tuplew
# w = list(x)
# w.pop(0)
# x = tuple(w)
# print(x)

# #7. Tuple constructor to createa tuple
# cities= tuple(("kampala","Jinja","Mbarara","Iganga"))
# print(cities)

# #8. unpack the tuple
# a,b,c,d = cities
# print(a)
# print(b)
# print(c)
# print(d)

# #9. range of indexes 2nd, 3rd and 4th
# print(cities[1:])


# #10. add two tuples
# first_name = ("Martha","Hellen","Hope")
# second_name =("Namugga", "Namiira","Agaba")
# print(first_name + second_name)

# #11. tuple of colours and multiply by 3
# colours = ("red","green","blue")
# print(colours*3)

# #12. number of times 8 appears
# thistuple = (1,3,7,8,7,5,4,6,8,5)
# print(thistuple.count(8))


# #    EXERCISE 3 (SETS)
# #1. set constructor with fav beverage
# Beverages= set({"soda","beer","coffee","juice"})
# print(Beverages)

# #2. add two or more items to set
# Beverages.add("tea")
# print(Beverages)

# #3. check if microwave is present
# mySet = {"oven","kettle","microwave","refrigerator"}
# if "microwave" in mySet:
#     print("Yes micrwave is present")

# #4. remove kettle from set
# mySet.remove("kettle")
# print(mySet)

# #5. loop through set above
# for x in mySet:
#     print(x)

# #6 adding elements in a list to elements in a set
# list1 = ["Martha","Hellen"]
# set1 = {"Luyombo","Namugga"}
# set1.update(list1)
# print(set1)

# #7. joining two sets of age and names
# names = {"Martha","Hellen","Hope"}
# ages = {23,25,30}
# print(names.union(ages))


# #   EXERCISE 4 (STRINGS)
# #1. concatinating string and int
# name = "martha"
# age = 13
# print(name+ " "+str(age))

# #2. remove space at beginning, middle and end
# txt = "  Hello,  Uganda!  "
# print(txt.strip) # remove trailing spaces

# #3, convert txt to upper case
# print(txt.upper())

# #4. replace U with V in the string above
# print(txt.replace("U","V"))

# #5. return chracters in the 2nd, 3rd and 4th positions
# y = "I am proudly Ugandan"
# print(y[1:3])

# #6. correct "all data scientists" are cool!"
# x = "All data scientist's are cool!"
# print(x)


# #     EXERCISE 5(DICTIONARIES)

# #1.print value of shoe size
# Shoes ={
#     "brand": "Nick",
#     "color": "black",
#     "size": 40
# }
# print(Shoes["size"])
# print(Shoes)

# #2.change value "Nick" to "Adidas"
# Shoes["brand"] = "Adidas"
# print(Shoes["brand"])

# #3.add key/value pair "type" to :sneakers
# Shoes["type"] = "sneakers"
# print(Shoes["type"])
# print(Shoes)

# #4, return all keys
# print(Shoes.keys())

# #5. return all values
# print(Shoes.values())

# #6. check if size exists
# if "size" in Shoes:
#     print("yes it does")
# else:
#     print("no")

# #7. loop through dictionary
# for key,value in Shoes.items():
#     print(key,  value)

# #8. remove colur from dictionary
# Shoes.pop("color")
# print(Shoes)

# #9. empty dictionary
# Shoes.clear()
# print(Shoes)

# #10. make a dictionary and make a copy of it
# myDict = {
#     "name": "Martha",
#     "age": 99,
#     "gender": "female"
# }
# myDict_copy = myDict.copy()
# print(myDict_copy)

# #11. show nested dictionaries
# person = {
#     "name": "Martha",
#     "age": 99,
#     "gender": "female",
#     "address": {
#         "city": "Kampala",
#         "state": "Uganda"
#     }
# }
# print(person)


# ----------------------------------------------------------------
#                     DAY 4

# FUNCTIONS
"""There is need for reusable, maintaonable code
syntax  :
def function_name():
    statements
    return value

Parameters and arguments
Parameters are variables that are passed to the function
Arguments are passed when the function is called
"""

# def greeting(first_name, last_name):
#     print(f"Hello {first_name} {last_name} nice to meet you!")

# greeting("Martha", "Hellen")

# def add(a, b):
#     return a + b

# print(f"Adding a and b gives us {add(3,6)}")

# #many arguments
# def sum_numbers(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# # Calling the function with different numbers of arguments
# print(sum_numbers(1, 2, 3,10))

# #no arguments
# def afternoon():
#     print("Good afternoon")
# afternoon()


# MODULES
# #a simple calc
# def add(s,w):
#     return s+w

# def subtract(s,w):
#     return s-w

# def multiply(s,w):
#     return s*w

# def divide(s,w):
#     return s/w


# #importing within the same file
# import martha_namugga_afternoon

# print(martha_namugga_afternoon.add(2,3))
# so you cannot import within the same file. They should be different files in the same folder


# Math module
# importing square root and factorial from the module math

# print(f"the square root of 16 is {sqrt(16)}")
# print(f"the factorial of 3 is {factorial(3)}")


#  INPUT AND OUTPUT
"""
syntax
input('prompt')
taes all input as strings by default
"""
# #Example
# name = input("Enter your name ")
# print(f"Hello {name} nice to meet you!! ")

# #Example 2
# number_one = int(input("Enter first number "))
# number_two = int(input("Enter second number "))
# print(f"The sum of {number_one} and {number_two} is {number_one+number_two}")

# #Example3. Multiple inputs in python
# s,r,w = map (int, input("Enter three values: ").split())
# print("the values are : ", end = " ")
# print(s,r,w)

# # capturing input in a tuple
# w = (2,4,6,8)
# print("Tuple before adding an element")
# print(w)

# y = list(w)
# #adding elemnt to the list
# y.append(int(input("Enter a value to tuple ")))
# print("Tuple after adding an element")
# w = tuple(y)
# print(w)

# my_list = list(map(int, input("Enter list values(space separated): ").split()))
# my_set = set(map(int, input("Enter set values: ").split()))

# print(my_list)
# print(my_set)


# ----------------------------------------------------------------
# DAY 5 (FRIDAY 30TH)


# EXCEPTION HANDLING
"""
execption handling is the process of handling errors
syntax
try:
    statements
except:
    statements
finally:
    statements

try block is used to monitor a code which we think will throw an error
we catch these excpetations
except block is used to handle exceptions
finally block runs regarless

types of exceptions
1. ZeroDivisionError: Raised when a division or modulo operation is performed with zero as the divisor.
2. TypeError: Raised when an operation or function is applied to an object of inappropriate type. ("10" + 5)
3. ValueError: Raised when a function receives an argument of the correct type but an inappropriate value.(int("abc"))
4. NameError: Raised when a local or global name is not found. (print(undefined_variable))
5. FileNotFoundError: Raised when a file or directory is requested but cannot be found.
6. IndexError: Raised when a sequence subscript is out of range.
7. KeyError: Raised when a dictionary key is not found.
8. AttributeError: Raised when an attribute reference or assignment fails.
9. ImportError: Raised when an import statement fails to find the specified module.
10. IOError: Raised when an input/output operation fails, such as when reading or writing to a file.

"""

# Example of exception handling
try:
    numbers = [1, 2, 3, 4, 5]
    print(numbers)
    index = int(input("Enter an index: "))
    value = numbers[index]
    print("Value at index", index, "is", value)

except IndexError:
    print("Error: Index out of range.")

finally:
    print("Finally block always executed")


# FILE HANDLING
"""
Allows one to work with files on a computer

things considered when dealing with file handling
1. Opening a file
  - open()
  - takes two parameters (filename, mode)
  - file = open("filename.txt", "r")

2. Reading a file 
  - there are different ways to read
  - read() -> reads entire content as a single string
  - readline() -> reads one line from the file
  - readlines() -> reads all lines from the file
  - content = file.read()

3. Writing a file
  - there are different ways to write
  - write() -> writes entire content as a single string
  - writelines() -> writes all lines from the file
  - file.write("hello world")

4. Closing a file
  - close a file after working on it
  - file.close()

5. Modes
    -"r": Read mode (default). Opens a file for reading.
   - "w": Write mode. Opens a file for writing. Creates a new file or overwrites the existing file.
   - "a": Append mode. Opens a file for appending. Writes data at the end of the file.
   - "x": Exclusive creation mode. Creates a new file but raises an error if the file already exists.
   - "t": Text mode (default). Opens a file in text mode.
"""

# Examples
# Writing to a file

try:
    file = open("writing.txt", "w")
    # Write data to the file
    file.write(input("Write the data you need saved in the file "))

    # Display a success message
    print("Data written to file successfully!")

except FileNotFoundError:
    print("Error: File not found")
except IOError:
    print("Error: Input/Output error")

finally:
    # Close the file
    file.close()

print("----------------------------------------------------------------")

# Reading from a file
try:
    file = open("writing.txt", "r")

    content = file.read()

    # Display the file content
    print("File Content:")
    print(content)

except FileNotFoundError:
    print("Error: File not found")
except IOError:
    print("Error: Input/Output error")
finally:
    file.close()
