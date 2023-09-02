import mysql.connector
print("create connections")
mydb = mysql.connector.connect(
    host="localhost",
    user="heet",
    password="Heet@12012001")
print(mydb)
print("Connection created")