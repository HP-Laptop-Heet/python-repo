#using the string functions
s="heet kumar"
print(s.capitalize())    # for capitalize the first letter of string

s="HEET kumar"
print(s.casefold())  # or use s.lower()   this used for converting the string in lower case

s="heet kumar"
print(s.center(30))   # giving space before printing the string

s="kumarheet kumar heet tony kumar"
print(s.count("kumar"))   # count the no. of times used particular string

s="heet kumar"
print(s.find("kumar"))   # tell the position of the starting word

s="heet kumar"
print(s.index("kumar"))  # tell the position of the starting word

s="heet kumar"
print(s.find("hi"))  # when result not found then it will return -1

s="heet kumar"
print(s.index("kumar"))   # when result not found then it shows error

s="heet123"
print(s.isalnum())     # it will check string is alpha-numeric and then give answer in true or false only
# in the above question we need not to give spacing   for only for above 1 question

s="123"
print(s.isalnum())   # o/p will be True

s="heet"
print(s.isalnum())  # o/p will be true

s="heet 123"
print(s.isalnum())   # bcz of spacing(special charachter) it will show the False

s="heet123"
print(s.isdigit())   # it will print False bcz it contain also alphabets

s="123"
print(s.isdigit())  # it will print true
'''
s=123
print(s.isdigit())  # Error only this isdigit function for checking into strings only
'''
s="heet123"
print(s.islower())  # it will print true

s="heet"
print(s.islower()) #it will print true

s="Heet123"
print(s.islower())  # it will print false bcz H

s="My name is Heet"
print(s.encode())      # for encode the other than the ascii leters

s="My name is Heet"
print(s.endswith("t"))   #True, checking the ending letter in string

s="My name is Heet"
print(s.endswith("."))  #False, checking the ending letter of the string