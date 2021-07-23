'''- A class is like a factory pattern:
- You take the "pattern" called class and build a "copy" object of the class by assigning the class call to a variable.  This "copy" is called "instance".
- The instance inherits all attributes and methods from class.
- The instance also holds its own "namespace" which means you can access instance attributes and methods from the instance itself without having to reference the parent class.
- To build this separate namespace on every instance you use a constructor method on the class which need 1 argument widely called self .
- self will reference the instance itself every time you create a new object from the "parent" class. But how is this required behavior explained?
- This means, internally every time you call an instance method you are calling the parent class and passing the instance to it so the class method takes the instance as a parameter and That's why class methods needs self as a required argument.
The computer takes advantage from reusing the class logic and passing only the changed values on the instance attributes so all the logic is not replicated. You must use self on constructor and every method to keep this logic only referenced and not replicated in memory.
So by calling a instance method, python takes the parent class feed it with the instance changes and reuses the methods replacing self with the instance changes and executing the logic.'''

from nameDemo import Demo2, Demo3
import sys
print(sys.path)
from com.cloudwick.PackageDemo import PackageDemo

class Demo:
     def __init__(self, connection):
          self.connection = connection
          print("Constructor called")

     def queryTable(self, tableName):
          print("querying provided table {0} using connection {1}".format(tableName, self.connection))

     def computeSum(self, a, b):
          print(__name__)
          self.sum = a + b
     def getSum(self):
          print("get sum called for parent class")
          print(self.sum)

     def withOutSelf(a):
          print("called with out self with parameter {0}" .format(a))

if __name__ == '__main__':
     print(__name__)

     demo = Demo("localhost:8080")
     demo.queryTable("students")

     demo1 = Demo("10.10.10.1:5673")
     demo1.queryTable("students")
     # demo1 = Demo()
     #demo2 = Demo2()
     # demo.computeSum(5, 3)
     # demo1.computeSum(6,5)
     # demo.getSum()
     # demo1.getSum()
     # #demo.withOutSelf(5)
     # Demo.withOutSelf(5)
     #
     # Demo.getSum(demo)
     # Demo.getSum(demo1)
     #
     #demo2.test()
     #
     #
     # demo3 = Demo3()
     # demo3.test()
     #
     #PackageDemo().check()
     #Test().call()