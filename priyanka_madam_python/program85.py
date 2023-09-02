# for loop with zip() function

questions=["name","quest","favorite color"]
answers=["lancelot","the holy grail","blue"]

for i,v in zip(questions,answers):
    print("what is your {0}? It is {1}.".format(i,v))

# zip function help us to print the two list elements with additional sentence into it prints together