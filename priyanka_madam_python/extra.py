import psycopg2
mydb=psycopg2.connect( user="postgres",password="Heet@12012001",host="127.0.0.1",port="5432")
c=mydb.cursor()
#c.execute('''create table hope(id int,name text,salary real);''')
c.execute("insert into hope (id,name,salary) values (301,'john',20000)");
c.execute("select * from hope")
print(c.fetchall())
mydb.commit()
mydb.close()