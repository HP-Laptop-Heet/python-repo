#inseting many values in table

import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="Heet@12012001")
c=conn.cursor()
c.execute("use mydatabase")
#c.execute("drop table customers")     # for deleting
#c.execute("create table customers1 ( name varchar(30), address varchar(100))")  # for creating table
c.execute("show tables")
for x in c:
    print(x)
c.execute("insert into customers values ('Sunil','Dosa,Rajasthan')")  #inserting values in table
conn.commit()
print(c.rowcount,"record inserted")
c.execute("select* from customers")     # for seeing the table
print(c.fetchall())
conn.close()