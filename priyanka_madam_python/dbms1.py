# this program only show how to use cursor

import mysql.connector    # calling the API
#establishing the connection
mydb = mysql.connector.connect(host="localhost",user="heet",password="Heet@12012001")
#creating a cursor object using the cursor() method
cursor = mydb.cursor()
#Dopiing database MYDATABASE if already exists.
cursor.execute("select database()")
#Fetch a single row using fetchone() method.
data=cursor.fetchone()   # fetchone is for taking details from mysql to pycharm
print("connection established to :",data)  # and then printing
#closing the connection
mydb.close()