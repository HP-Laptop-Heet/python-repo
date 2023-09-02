#exception handling with finally

try:
    print("Hello")
    print(a)                              # error will occur bcz a was not declare   and then make  print(a) as comment
except:
    print("Something went wrong")
finally:
    print("Nothing went wrong")

    #  finally will run in any cost if error occurs or not it dosen't matter for finally