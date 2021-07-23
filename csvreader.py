import csv

class csvreader:
     """
     Class containing csv handlers
     """
     def read_Csv(self, file):
          """
          function to read csv file
          :param file: file name
          :return:
          """
          f = open(file)
          csv_f = csv.reader(f)

          for row in csv_f:
               name,city,phone=row
               print("Employee {0} belongs to {1} and his contact is {2}".format(name, city, phone))

     def write_csv(self, employees):
          with open('employees.csv','w') as f:
               csvw = csv.writer(f)
               csvw.writerows(employees)

     def read_csv_dict(self, file):
          fp = open(file)
          reader=csv.DictReader(fp)
          for row in reader:
               print("Dict reader: Employee {0} belongs to {1} and his contact is {2}".format(row['name'], row['city'], row['phone']))

     def write_csv_dict(self, data: dict):
          with open('employees_dict.csv','w') as ed:
               csvd = csv.DictWriter(ed, fieldnames=data[0].keys())
               csvd.writeheader()
               csvd.writerows(data)

ob = csvreader()
ob.read_Csv('file.txt')
ob.write_csv([['Venkat','Hyderabad','Nike'],['Bharat','Hyderabad','Nike']])
ob.read_csv_dict('file_header.csv')
ob.write_csv_dict([{'name':'Bharat','city':'Hyderabad','phone':'7794994702'}])