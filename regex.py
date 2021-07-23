'''regular expressions are used to search a string or a pattern in a string'''

import re

message = "2021-07-16 hostname [1234] server is getting started"

result = re.search(r"\[(\d+)\].*\[(\d+)\]", "info [12345] number is [456] check")
print(result)

#using grep to find regex patterns in a file both case sensitive and case insensitive

# dot(.) is a special character that is used as a wildcard and represents matching with any character

#^ is a special character to represent start of a line
#$ is a special character to represent end of line

result = re.search(r"eck", "CheCk")

result = re.search(r"eck", "CheCk", re.IGNORECASE)
print(result)

str= "the end of higHway"

result = re.search("[a-zA-Z]way", str)

print(result)

result = re.search(r"[pP]ython","Python")
print(result)

str = "this is the way to go"

result = re.search("[a-z]way", str)

print(result)

result = re.search("cloud[a-zA-z0-9]", "cloudy")
print(result)

result = re.search("cloud[a-zA-z0-9]", "cloud9")
print(result)

str="This is a sentence with spaces."
# Not match
result = re.search("[^a-zA-z ]", str)
print(result)

print(re.search(r"^this","this is a good one"))

result = re.search(r"cat|dog", "These are cats")
print(result)

result = re.search(r"cat|dog", "These are dogs")
print(result)

result = re.search(r"cat|dog", "These are cats and dogs")
print(result)

result = re.findall(r"cat|dog", "These are dogs and cats")
print(result)


#* takes any characters as possible

print(re.search("c.*s", "i like cats"))

print(re.search("py[a-z]*n", "python programming"))

#0 or more occurences
print(re.search("py[a-z]*n", "pyn"))

#1 or more occurences
print(re.search("py[a-z]+n", "python"))

print(re.search("py[a-z]+n", "pyn"))

#either zero or one occurence
print(re.search(r"p?each", "each"))
print(re.search(r"p?each", "peach"))


print(re.search(r"\.com", "domain.com"))

#\w \s \d

#Passwords that should not start with digits


re.split(r"[.?!]", "one sentence. another one? and the last one!")

print(re.sub(r"\[REDACTED\]","bharath.8199@gmail.com","Received an email from [REDACTED]"))

# write a password validator

#should start with a upper case letter and
# should contain atleast one digit and
# should contain any of special character like @
# should not be more than 15 characters

def validatePassword(password):
     result = re.match(r"[A-Z].*", password)
     if result == None:
          return "Password should be started with a upper case letter"
     result = re.match(r".*[0-9]+.*", password)
     if result == None:
          return "Password should have atlease one digit between zero to 9"
     result = re.match(r".*[^0-9A-Za-z ].*", password)
     if result == None:
          return "Password should have atlease one special character"
     if len(password) > 15:
          return "Password length should be greater than 15"

     return "Password validated"

print(validatePassword("Bharat@123"))
print(validatePassword("9jsbdkfsfbjkhasbdh"))