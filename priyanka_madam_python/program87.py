#using for loop with sorted() function

basket=["apple","orange","apple","pear","orange","banana"]

for i in sorted(set(basket)):
    print(i)

# in  this we are printing the elements in sorted manner and also repetition is not allowed