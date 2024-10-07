


# Datatypes
# string = 'Hello World'    # string
# integer = 13
# float = 13.5
# boolean = True

# myList = ["list", "list2", "List3"]
# myTuple = ("immutable")
# myDictionary = {"Name1" : "Brian", "Address" : "My Home"}
# mySet = {"Apples", "Pears", "Apples"}

# print(myDictionary.values())
# myDictionary["Name1"] = "Luke"
# myDictionary["Name2"] = "Brad"
# print (myDictionary)


# for name in myTuple:
#   print(name)


# Operators

# > greater than
# < less than
# == equivelant
# != not equal to
# >= greater than or equal
# <= less than or equal
# + Addition
# - Subtraction
# * Multiplication
# / Division
# % Modulus


# print(5 % 3)


# list2 = [1,3,5,7,10,12,14]

# for number in list2:
#   # print(number)
#   if number % 2 != 1:
#     print (number)

# for strings in myList:
#   for string in strings:
#     print (string)



# list3 = ["Brian", "Dan", "Justin", "Bob"]


# if "5"  in "453":
#   print("true")

# for i in range(0,10,2):
#   print(i)


# i = 0

# while i <= 100:
#   print(i)
#   i += 1


# adj = ["red", "green", "tasty"]
# fruits = ["apple","banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x,y)




# strVariable = input("Hello, Please insert your name: ")
# variable2 = "String"

# print (f"Hello, my name is {strVariable}") f string

# intVariable = input("Please insert a number: ")
# print (int(intVariable) + 10)

# int String Float Boolean List Tuple Dictionary Set 

# list

myList = ["Dan", "Brian", "Justin", "Bob"]
#            0       1       2         3

# count = len(myList)

# print(count)

# for name in myList:
#   print(f"Hello my name is {name}")

# myList[2] = "Luke"
# print(myList)

# Brad = False

# for name in myList:
#   if name == "Brad":
#     myIndex = myList.index(name)
#     myList[myIndex] = "Luke"
#     Brad = True

# if Brad != True:
#   myList.append("Brad")




# myList.append("Luke")

# print (myList)


# Functions

# def my_function():
#   print("Hello World")

# my_function()

# circle area = pi(r^2)

# def areaOfCircle(radius):
#   area = 3.14 * radius ** 2
#   return area

# def mathematicalOperation(number):
#   area = areaOfCircle(7)
#   operation = number + area
#   return operation

# print(mathematicalOperation(5))



# def multiple(*numbers):
#   value = 0
#   for number in numbers:
#     value += number
#   return value

# print(multiple(3, 4, 5, 6, 7))


# def children(child1, child2, child3):
#   print(child2)

# children("Brian", "Dan", "Scott")

# print(abs(-7.5))
# print(int())
# print(dict(name = "Brian", Age = 25))
# print(pow(5, 5))
# math = 55 / 3

# print(f"{math:.2f}")

# Here are a list of the most common built-in functions in Python with examples:

# abs() - returns the absolute value of a number

# x = abs(-7.25)
# print(x)

# # all() - returns True if all items in an iterable object are true. an item is true if it is not 0, None, empty, or False

# list1 = [1, 2, 3, 4]
# print(all(list1))

# # any() - returns True if any item in an iterable object is true

# list1 = [0, 1, 2, 3]
# print(any(list1))

# # ascii() - returns a readable version of an object.  It will replace any non-ascii characters with escape characters

# x = ascii("My name is Ståle")
# print(x)

# # bin() - returns the binary version of a number

# x = bin(5)
# print(x)

# # bool() - returns the boolean value of the specified object.  an object is true if

# x = bool(5)
# print(x)

# # bytearray() - returns an array of bytes. this is useful for converting integers to bytes which can be used for hashing algorithms

# x = bytearray(5)
# print(x)

# # bytes() - returns a bytes object this is useful for converting integers to bytes which can be used for hashing algorithms

# x = bytes(5)
# print(x)

# # callable() - returns True if the specified object is callable, otherwise False

# def x():
#     print("hello")

# print(callable(x))

# # chr() - returns a character from the specified Unicode code.

# x = chr(61)
# print(x)

# # dict() - returns a dictionary (Array)

# x = dict(name="John", age=36)
# print(x)

# # enumerate() - takes a collection (e.g. a tuple) and returns it as an enumerate object

# x = ('apple', 'banana', 'cherry')
# y = enumerate(x)
# print(list(y))

# # eval() - evaluates and executes an expression

# x = 'print(55)'
# eval(x)

# # exec() - executes the specified code (or object)

# x = 'print(55)'
# exec(x)

# # filter() - use a filter function to exclude items in an iterable object

# def x(a):
#     if a < 5:
#         return False
#     else:
#         return True
    
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = filter(x, list1)
# print(list(list2))

# # float() - returns a floating point number

# x = float(5)
# print(x)

# # format() - formats a specified value

# x = format(0.5, '%')
# print(x)

# # getattr() - returns the value of the specified attribute (property or method)

# class Person:
#     name = "John"
#     age = 36
#     country = "Norway"

# x = getattr(Person, 'age')
# print(x)

# # help() - executes the built-in help system

# help(print)

# # input() - allows user input

# x = input("Enter your name: ")
# print("Hello, " + x)

# # int() - returns an integer number

# x = int(5.5)
# print(x)

# # isinstance() - returns True if a specified object is an instance of a specified object

# x = isinstance(5, int)
# print(x)

# # issubclass() - returns True if a specified class is a subclass of a specified object

# class Person:
#     name = "John"
#     age = 36
#     country = "Norway"

# class Student(Person):
#     pass

# x = issubclass(Student, Person)

# print(x)

# # len() - returns the length of an object

# x = len("Hello World")
# print(x)

# # list() - returns a list

# x = list(("apple", "banana", "cherry"))
# print(x)

# # map() - returns the specified iterator with the specified function applied to each item

# def x(a):
#     return a * a

# list1 = [1, 2, 3, 4]
# list2 = map(x, list1)
# print(list(list2))
# # this function is mapping the function x to each item in list1, it maps 1 to x, 2 to x, 3 to x, and 4 to x, and returns a list of the results. 

# # max() - returns the largest item in an iterable

# x = max(5, 10, 15)
# print(x)

# # min() - returns the smallest item in an iterable

# x = min(5, 10, 15)
# print(x)

# # next() - returns the next item in an iterable

# list1 = [1, 2, 3, 4]
# list2 = iter(list1)
# print(next(list2))

# # pow() - returns the value of x to the power of y

# x = pow(4, 3)
# print(x)

# # print() - prints to the standard output device

# print("Hello World")

# # property() - gets, sets, deletes a property

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def x(self):
#         print("Hello my name is " + self.name)
    
#     def y(self):
#         print("I am " + str(self.age) + " years old")

# x = property(Person.x, Person.y)
# print(x)

# # range() - returns a sequence of numbers, starting from 0 by default, and increments by 1 by default, and ends at a specified number.  start, stop, step are used in the parentheses to specify the start, stop, and step values of the range being used

# for i in range(0,6,1):
#     print(i)

# # reversed() - returns a reversed iterator

# list1 = [1, 2, 3, 4]
# list2 = reversed(list1)
# print(list(list2))


# # round() - rounds a numbers

# x = round(5.76543, 2) # (number, number of decimal places)
# print(x)

# # set() - returns a new set object

# x = set(("apple", "banana", "cherry"))
# print(x)

# # sorted() - returns a sorted list

# list1 = [1, 2, 3, 4]
# list2 = sorted(list1)

# # str() - returns a string object

# x = str(5)
# print(x)

# # sum() - sums the items of an iterator

# list1 = [1, 2, 3, 4]
# x = sum(list1)

# # super() - returns an object that represents the parent class

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
    
#     def printname(self):
#         print(self.fname, self.lname)

# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)

# x = Student("John", "Doe")

# # tuple() - returns a tuple

# x = tuple(("apple", "banana", "cherry"))
# print(x)

# # type() - returns the type of an object

# x = type(5)
# print(x)

# # zip() - returns an iterator, from two or more iterators

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# list3 = zip(list1, list2)
# print(list(list3))

