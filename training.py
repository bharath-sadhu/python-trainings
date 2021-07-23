'''An interpreter is a kind of program that executes other programs.
When you write Python programs , it converts source code written by the developer into intermediate language
which is again translated into the native language / machine language that is executed.
The python code you write is compiled into python byte code,
which creates file with extension .pyc . The byte code compilation happened internally,
and almost completely hidden from developer. Compilation is simply a translation step,
and byte code is a lower-level, and platform-independent , representation of your source code. Roughly,
each of your source statements is translated into a group of byte code instructions.
This byte code translation is performed to speed execution byte code can be run much quicker than the original source code statements.'''



'''Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview'''


x = 5
print(type(x))



x = "Hello World"
x = 20
x = 20.5
x = 1j
x = ["apple", "banana", "cherry"]
x = ("apple", "banana", "cherry")
x = range(6)
x = {"name" : "John", "age" : 36}
x = {"apple", "banana", "cherry"}
x = frozenset({"apple", "banana", "cherry"})
x = True
x = b"Hello"
x = bytearray(5)

print(x)

# Python program to understand
# use of frozenset function

# creating a list
favourite_subject = ["OS", "DBMS", "Algo"]

# making it frozenset type
f_subject = frozenset(favourite_subject)

# below line will generate error

#f_subject[1] = "Networking"



'''The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion.
Python has two types of type conversion.

Implicit Type Conversion
Explicit Type Conversion


Implicit Type Conversion
In Implicit type conversion, Python automatically converts one data type to another data type. This process doesn't need any user involvement.

Let's see an example where Python promotes the conversion of the lower data type (integer) to the higher data type (float) to avoid data loss.'''

# Implicit Type Conversion
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

#Explicit type conversion/ type casting

num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))

#print(num_int+num_str)


#fix explicit typr conversion with user define casting functions int(), float(), str() e.t.c

num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))


#defining functions with return value
def sum(a, b):
     return a+b

print(sum(3,5))


#if else
a=5
i = 5 if a > 7 else 0
print(a)


#demonstration of elif
'''In this program, 
we check if the number is positive or
negative or zero and 
display an appropriate message'''

num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


'''In this program, we input a number
check if the number is positive or
negative or zero and display
an appropriate message
This time we use nested if statement'''

num = float(4)
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")



#loops in python

'''While Loop: 
In python, while loop is used to execute a block of statements repeatedly until a given a condition is satisfied. 
And when the condition becomes false, the line immediately after the loop in program is executed. 
Syntax :

while expression:
    statement(s)
        3. All the statements indented by the same number of character spaces after a programming construct are considered to be 
        part of a single block of code. Python uses indentation as its method of grouping statements. 
            Example: '''


# Python program to illustrate
# while loop
count = 0
while (count < 3):
	count = count + 1
	print("Hello Everyone")


# Python program to illustrate
# Iterating over range 0 to n-1

n = 4
for i in range(0, n):
	print(i)


# Python program to illustrate
# Iterating by index

list = ["cloudwick", "technologies"]

#parse by index
for index in range(len(list)):
	print(list[index])

#Parse by element
for a in list:
     print(a)




'''capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case'''

#Strings are immutable, All string methods returns new values. They do not change the original string.

#multi-line string

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#strings are arrays
a = "Hello, World!"
print(a[1])


#looping through a string

for x in "banana":
  print(x)

#string length

a = "Hello, World!"
print(len(a))

#check is sub-string is present in string
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#slicing
b = "Hello, World!"
print(b[2:5])

#slice from start
b = "Hello, World!"
print(b[:5])

#slice to end
b = "Hello, World!"
print(b[2:])



'''Negative Indexing
Use negative indexes to start the slice from the end of the string:
Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):'''

b = "Hello, World!"
print(b[-5:-2])


#to upper case
a = "Hello, World!"
print(a.upper())


#to lower case
a = "Hello, World!"
print(a.lower())

#remove white spaces
a = " Hello, World! "
print(a.strip())

#replace string
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#sting concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)



#Use the format() method to insert numbers into strings:
age = 36
#error = "My name is John, I am " + age
txt = "My name is John, and I am {}"
print(txt.format(age))


#multiple substitutions
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#Escape characters

'''Code	Result
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value'''


txt = "We are the so-called \"Vikings\" from the north."
print(txt)


'''Python has a set of built-in methods that you can use on lists/arrays.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list'''



list=[1,2,3]

list.append(4)
print(list)
list1=list.copy()
print(list1)

print(len(list))
list.extend(list1)
print(list)

print(list.index(2))

# insert number 8 at 4th position
list.insert(4,8)
print(list)
list.sort(reverse=True)
print(list)

list.remove(8)

print(list)

list.pop(1)

print(list)

list.reverse()

print(list)

list1.clear()

print(list1)

'''Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary'''

mydictionary = {'a':1, 'b':2, 'c':3}

print(mydictionary.get('a'))
mydictionary['d'] = 4

print(mydictionary)

print(mydictionary.items())

mydictionary.pop('d')

print(mydictionary)

mydictionary.update(d=4, c=5)

print(mydictionary)

d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)

#parsing list, touple and dictionary

#parsing list
list=['a','b','c']
for element in list:
     print(element)

#parsing touple
touple = (1,2,3,4)
for element in touple:
     print(element)

list_of_touples = [(1,2),(3,4)]

for x,y in list_of_touples:
     print('{0}:{1}'.format(x,y))

for a in mydictionary:
     print('{0}:{1}'.format(a, mydictionary.get(a)))