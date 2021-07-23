import configparser
import argparse
import sys

class readFile:
     def readFile(self):
          #file opened in read mode
          with open('sample.txt', mode='r') as f:
               for line in f:
                    print(line)
               f.close()
     def writeFile(self):
          with open('sample.txt', mode='r') as f:
               self.content = f.readlines()
               f.close()
          with open('sample_write.txt', mode= 'w', encoding='UTF-8') as f:
               for line in self.content:
                    f.write(line)
               f.close()
     def readProperties(self):
          config = configparser.ConfigParser()
          config.read('properties.ini')
          print(config.sections())
          print(config['DEFAULT']['Compression'])

     def readLineByLine(self):
          myfile = open("sample.txt", "r")
          while myfile:
               line = myfile.readline()
               print(line)
               if line == "":
                    break
          myfile.close()

if __name__ == '__main__':
    ob = readFile()
    ob.readFile()
    ob.readLineByLine()
    ob.writeFile()
    ob.readProperties()

    # parser = argparse.ArgumentParser(description='Process some integers.')
    # parser.add_argument('--name', type=str, help= "Provide name")
    # parser.add_argument('--age', type=int, help= "Provide age")
    # args = parser.parse_args()
    # print('Hi, i am {0} and i am {1} years old'.format(args.name, args.age))


