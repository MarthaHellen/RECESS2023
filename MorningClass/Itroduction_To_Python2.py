#import threading
#import multiprocessing
# import re
from contextlib import contextmanager
"""
THIS IS THE CONTINUATION OF THE PREVIOUS FILE BECAUSE IT HAD BECOME EXTREMELY LONG
(martha_namugga1. py)
"""

# ----------------------------------------------------------------

"""
                    DAY 6
   ADVANCED TOPICS IN PYTHON
1. Regular expressions
2. generators and iterators
3. decorators
4. Context managers
5. Multithereading and multiprocessing

"""

# REGULAR EXPRESSIONS

"""
Regular expressions (regex) are a form of pattern matching.
They are used to find patterns in text.
r = at the beginning is for regular expressions
\b: is for line breaks
\d: match any digit (0-9)
\w: match any alphanumeric character (a-z, A-Z, 0-9 and underscore)
\s: match any whitespace character(space, tab, newline)
.: match any character except a new line
*: match zero or more occurrences of the preceding chracter or group
+: match one or more occurrences of the preceding character or group
?: match zero or more occurrences of the preceding character or group
[ ] : match any character within the squar bracket
[^ ] : match any character not within the square bracket
^ : matches the start of the line
$ : matches the end of the line
    
Matching and searching
#regex re.match(). re.search(), re.findall()

"""

# #Example 1.
# #Demonstrating regex |Match First word, Match Group world, Match all numbers
# text = "Hello, my name is Martha Nmaugga. I am a programmer with 10 years of experience"

# # Match First word
# match = re.search(r"\b\w+\b", text)

# if match:
#     print ("Matches: " ,match.group())

# #match digit
# matches = re.findall(r"\b\d+\b", text)
# print (f"Matches: {matches}")

# #using a patter
# pattern =  r"Martha"
# Match = re.search(pattern, text)
# print (f"Matches: {Match}")


# Example 2.
# Validating a simple email format or email address
# martha123@gmail.com

# def validate_email(email):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     if re.match(pattern, email):
#         return True
#     else:
#         return False

# #usage
# email1 = "martha-hellen@gmail.com"
# email2 = "martha123@gmail.com"
# email3 = "martha123@gmailcom"

# print(validate_email(email1))
# print(validate_email(email2))
# print(validate_email(email3))


# GENETRATORS AND ITERATORS
"""
generators help us repeat things
'yeild' : generators
iterators that implement iterator objects '__iter__' "__next__"
"""

# #Generator
# def factorial(n):
#     #return the factorial of a number
#     if n==0 :
#         return 1
#     else:
#         return n * factorial(n-1)

# #print the factorial of a numbers (1 to 10)

# for i in range(1,10):
#     print(factorial(i))


# Example 3
# def factorial(n):
#     # return the factorial of a number
#     if n == 0:
#         yield 1
#     else:
#         # yield n * factorial(n-1)
#         fact = 1
#         for i in range(1, n+1):
#             fact *= i
#         yield fact

# # #print the factorial of a numbers (1 to 10)

# for i in range(1, 10):
#     print(factorial(i))


# Example 3
# generate a function that yield the square of a number from 1 to 10

# def squares():
#     for i in range(1, 10 ):
#         yield i **2

# # crete an iterator object that yields the square of numbers from 1 to 10
# squares_iterator = squares()

# # print the first 5 numbers of numbers 1 to 10
# for i in range(5):
#     print(next(squares_iterator))


# DECORATORS
# Decorators in python allows you to modify the behavior of functions or classes without
# directly changing their source code

# def my_decorator(func):
#     def inner():
#         print("This is the decorator")
#         func()
#     return inner

# @my_decorator
# def outer_decorator():
#     print("This is the outer decorator")

# outer_decorator()

# Decorator
# '@decorator_name' is the name of the decorator

# Example 2
# it takes another function as input and modifies it. commonly used for authentication and logins

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         #code to be executed before the origianl function
#         print("This is the decorator before function execution")
#         result = func(*args, **kwargs)
#         #code to execute after the origianl function
#         print("This is the decorator after function execution")
#         return result
#     return wrapper

# @my_decorator

# def my_function():
#     print("This is the function")

# my_function()

# #Example 3
# def my_decorator(cls):
#     class ModifiedClass:
#         def __init__(self, *args, **kwargs):
#             self.instance = cls(*args, **kwargs)

#         def my_method(self):
#             print("Modified method")

#     return ModifiedClass

# @my_decorator
# class MyClass:
#     def my_method(self):
#         print("My original method")

# my_instance = MyClass()
# my_instance.my_method()

# ----------------------------------------------------------------

#          CONTEXT MANAGERS
# context manager is an object that defines context of a block of code
# Helps us ensure that resources are released properly
# Make code readable

# Example 1. Demonstrate a context manager to open a file  and return a context manager instance

# def open_file(filename):
#     #open the file and return a context manager instance
#     file = open(filename, "r")

#     def __enter__():
#         return file

#     def __exit__(self, exc_type, exc_value, exc_tb):
#         file.close()

#         return __enter__, __exit__

# #with statement helps the context to open the file
# with open_file("my_file.txt") as f:
#     contents = f.read()

# Example 2 context manger using a time series

# import time
# class Timer:
#     def __enter__(self):
#         self.start_time = time.time()

#     def __exit__(self, exc_type, exc_value, traceback):
#         end_time = time.time()
#         execution_time = end_time - self.start_time
#         print(f"The time for execution is {execution_time} seconds")

# #with example usage
# with Timer():
#     #meaures execution time
#     time.sleep(2)


# MULTITHREADING AND MULTIPROCESSING
"""
Two techniques used to improve performanceof the program

Multihreading is a techique where multiple threads are created within a single process
Multiprocessing is a teachnique where multiple processes are created

factors considered
- cores
- tasks
"""

# # Example of Multithreading

# def task(name):
#     print(f"Running task {name}")

# #creating multiple threads
# threads = []
# for i in range(10):
#     t = threading.Thread(target=task, args=(f"threads {i} ",))
#     threads.append(t)
#     t.start()

# #wait for all threads o finsh before it joins
# for t in threads:
#     t.join()


# Example of multiprocessing

# def process(name):
#     print(f"Processing task {name}")


# # create a pool of processes
# pool = multiprocessing.Pool(processes=5)

# # submit multiple task to the pool
# for i in range(6):

#     pool.apply_async(process, args=(f"Process {i}",))

# # close the pool and wait for all processes to finish
# pool.close()
# pool.join()


# # Example 5 Demonstration of multithreading and multiprocessing

# def task(name):
#     print(
#         f" Running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")

# #create multiple threads to run
# threads = []

# for i in range(4):
#     t = threading.Thread(target=task, args=(f"Thread {i}",))
#     threads.append(t)
#     t.start()

# #waiting for all threads to finish
# for t in threads:
#     t.join()







#ASSIGNMENT 7
"""
1a) Show a context manager for file handling that automatically opens and closes a file.
b) Shows a context manager for managing a database connection.
c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time
"""

#1a) 
class FileHandle:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileHandle("file.txt", "w") as file:
    file.write("This is Martha's file!")




#b)
import sqlite3

class DatabaseConnection:
    def __init__(self, file_name: str,):
        self.file_name = file_name
        self.connection = sqlite3.connect(self.file_name)

    def __enter__(self):
        print("DatabaseConnection")
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
       print("DatabaseConnection calling exit")
       self.connection.commit()
       self.connection.close()

# Example usage
with DatabaseConnection("university.db") as cursor:
    #creating a table if it doesn't exist
    create_table = '''
    CREATE TABLE IF NOT EXISTS student (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        year INTEGER,
        course VARCHAR(100)
    )
    '''
    cursor.execute(create_table)

    # Inserting data into the table
    insert = '''
    INSERT INTO student (name, year, course)
    VALUES ('Martha hellen', 1, 'BSSE'),
           ('luyombo', 2, 'BSSE'),
           ('Andrew', 4, "BCOM")
    '''
    cursor.execute(insert)

    cursor.execute("SELECT * FROM student")
    results = cursor.fetchall()
    for row in results:
        print(row)


# #c)

import time
import threading
from multiprocessing import Process

# Function to run
def run_function(name, seconds):
    print(f'Starting {name} for {seconds} seconds')
    time.sleep(seconds)
    print(f'{name} finished')

# Multithreading example
def multithreading_example():
    # List of threads
    threads = []

    # Create and start threads with different durations
    threads.append(threading.Thread(target=run_function, args=('Thread 1', 3)))
    threads.append(threading.Thread(target=run_function, args=('Thread 2', 5)))
    threads.append(threading.Thread(target=run_function, args=('Thread 3', 2)))

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Multiprocessing example
def multiprocessing_example():
    # List of processes
    processes = []

    # Create and start processes with different durations
    processes.append(Process(target=run_function, args=('Process 1', 3)))
    processes.append(Process(target=run_function, args=('Process 2', 5)))
    processes.append(Process(target=run_function, args=('Process 3', 2)))

    # Start the processes
    for process in processes:
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

# Run the multithreading example
multithreading_example()

# Run the multiprocessing example
# multiprocessing_example()










#----------------------------------------------------------------

                #DAY 7. PYTHON FOR DATASCIENCE

""" 
1. NumPy - Python library for numerical computing
2. Pandas - Fuctionalities
          * data cleaning
          * transformation
          * merging
          * filtering

Data Visualization
Plotiing - use library called matplotlib or seabon -> to create line, scatter, bar, histograms
heat maps

key concepts in data Science:
1. Data - (text, images, videos) or semi structured data (JSON, XML)
2. Data Mining
3. Machine learning
4. statistical Analysis
5. Big data
7. Predictive Analysis

"""

""""
UNDERSTANDING DATA SCIENCE WORK FLOW

1. Problem definition
2. Data Acquisition data.gov, kaggle, data bases, APIs, external data sets
Ensure data quality, data validation, cleaning and processing

#EDa -> Data exploratory analysis

#data Preparation and preprocessing
- Missing data
-Wrong format
- Null values
- Duplicates
"""

