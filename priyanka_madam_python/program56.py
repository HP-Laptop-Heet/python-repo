# passing the list in the function
def unique(l):  # l is here list
    x=[]          # x is new empty list
    for i in l:                   # "i" is element not a position
        if i not in x:            # "i" is element not a position
            x.append(i)   # through append function we are adding element in x

    return x

u_list=[1,2,3,2,1,4,5]
d=unique(u_list)
print(d)        # in python it is not neccessary we need to store the return value we can directly print that command also