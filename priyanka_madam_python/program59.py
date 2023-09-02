# program to reverse a string using function
def string_reverse(s):
    rs=""
    l=len(s)
    for i in range(0,l):
        rs=rs+s[-i-1]
    return rs

st=str(input("Enter the string : "))
print(string_reverse(st))