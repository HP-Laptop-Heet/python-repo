# creating the file
''' modes are r=read,w=write,a=append,x=creating file'''

f=open("myfile.txt","r")
print(f.readline())
print(f.readline())
f.close()

# read() function for the reading the total data in the file
#readline() function for the read only line