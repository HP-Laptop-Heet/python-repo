# printing the pattern using nested for loop

n=5
for i in range(0,n):
    for j in range(0,i+1):
        print(i,end=" ")           # end=" " is for continuation print in one line
    print("")                      # this print for going in next line

                #if we don't use end=" " the print command always print in next line always.
                #for continues print in one line so we need to use it end=" "