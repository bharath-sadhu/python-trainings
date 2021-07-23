class Demo2:
     def test(self):
          print("This is to demonstrate use of {0}".format(__name__))

class Demo3:
     def test(self):
          print("This is to demonstrate multiple class in a single file and name gets resolved to {0}".format(__name__))

if __name__ == '__main__':
    demo = Demo2()
    demo.test()