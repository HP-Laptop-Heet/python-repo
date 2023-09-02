# creating the file and appending into the file and write into the file

'''f=open("19BCE10301.txt","x")     # this statement is used for only create the file but oncee you have created
f.close()'''                        # then again you have writen this statement then it shows error
f=open("19BCE10301.txt","w")
f.write("Hitu")
f.close()
f=open("19BCE10301.txt","a")
f.write("\nHeet kumar")
f.close()
f=open("19BCE10301.txt","r")
print(f.read())
f.close()
