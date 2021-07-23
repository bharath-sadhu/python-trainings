class A(object):
    def foo(self):
        print('A.foo()')

class B(object):
    def foo(self):
        print('B.foo()')

class C(B, A):
     def seeMethodResolution(self):
          print(C.mro())

ob = C()
ob.foo()
ob.seeMethodResolution()