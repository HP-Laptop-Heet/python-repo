# creating the database

import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="Heet@12012001")
c = mydb.cursor()
# deletion of the database with if condition
c.execute("drop database if exists mydatabase")
c.execute("create database mydatabase")
print("list of database :")
c.execute("show databases")
print(c.fetchall())               # fetchall() for fetching all the data
mydb.close()                      # fetchone() for fetching only one row