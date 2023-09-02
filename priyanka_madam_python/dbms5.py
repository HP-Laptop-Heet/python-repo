#insert multiple data in table

import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="Heet@12012001")
c=conn.cursor()
c.execute("use mydatabase")
sql = "insert into customers values"
val=[
    ('Manish','Rajkot,Gujarat'),
    ('Amit','Lucknow,UP'),
    ('Mayank','BHU,UP'),
]
c.executemany(sql,val)
conn.commit()
print(c.rowcount,"record was inserted.")
c.execute("select name,address from customers")
c=(c.fetchall())
for i in c:
    print(i)
conn.close()