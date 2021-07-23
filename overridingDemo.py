'''1.) *args

The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function.
It is used to pass a non-key worded, variable-length argument list.

The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined.
 With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
For example : we want to make a multiply function that takes any number of arguments and able to multiply them all together. It can be done using *args.
Using the *, the variable that we associate with the * becomes an iterable meaning you can do things like iterate over it,
run some higher-order functions such as map and filter, etc.'''


'''2.)**kwargs

The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. 
We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).

A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. 
That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.'''

from classDemo import Demo
import sys

class OverridingDemo(Demo):
     def __init__(self, hostname):
          super().__init__()

     def computeSum(self, a, b):
          self.sum = 2*(a + b)
     # def getSum(self):
     #      print("method in overriding Demo")
     #      print(self.sum)

     #Python doesn't support below type of method overloading
     '''     def computeSum(self, a, b, c):
                    self.sum = a + b + c'''
     #Method overloading can be done like below

     # Python program to illustrate
     # *args for variable number of arguments
     def myFun(self, *argv):
          for arg in argv:
               print(arg)

     # Python program to illustrate
     # *kargs for variable number of keyword arguments

     def myFun1(self, **kwargs):
          print(kwargs.keys())
          print(kwargs.values())
          for key, value in kwargs.items():
               print("%s == %s" % (key, value))

     def combineArgskwargs(self, *args, **kwargs):
          for arg in args:
               print(arg)
          print(kwargs.keys())
          print(kwargs.values())

if __name__ == '__main__':
     print(sys.argv)
     odDemo = OverridingDemo()
     odDemo.computeSum(5,8)
     odDemo.getSum()
     # odDemo.myFun('Hello', 'Welcome', 'to', 'Cloudwick')
     # odDemo.myFun(1,2,3,'hello',5,'check')
     # odDemo.myFun1(first='Geeks', mid='for', last='Geeks')
     # odDemo.myFun1(start=0, end=100)
     # odDemo.combineArgskwargs(1,2,3,4,5, start=0, end=100)
