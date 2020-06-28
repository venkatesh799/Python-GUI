import sqlite3  #importing 
conn=sqlite3.connect("database.db")  #creating databse
c=conn.cursor()  #eastablishing connection with database
c.execute('create table stocks(Item text,Price real)')  #creating table

#inserting single Entry
c.execute("insert into stocks values('Computer',30000)")

#inserting many
purchases=[('Laptop',40000),('Keyboard',500),('Mouse',400)]
c.executemany("insert into stocks values(?,?)",purchases)

conn.commit()  #saving All Changes

conn.close()   #Closing Connection


