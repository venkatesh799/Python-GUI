import sqlite3  #importing 
conn=sqlite3.connect("database.db")  #creating databse
c=conn.cursor()  #eastablishing connection with database
c.execute('create table stocks(Item text,Price real)')  #creating table

#inserting single Entry
c.execute("insert into stocks values('Computer',30000)")

#inserting many
purchases=[('Laptop',40000),('Keyboard',500),('Mouse',400)]
c.executemany("insert into stocks values(?,?)",purchases)

#fetch using iterator
print("Before Updating")
for row in c.execute("select *from stocks"):
    print(row)

#Updating Records
c.execute("update stocks set item='None' where  price > 25000")

print("After Updating")

for row in c.execute("select *from stocks"):
    print(row)

conn.commit()  #saving All Changes

conn.close()   #Closing Connection

'''
OUTPUT

Before Updating
('Computer', 30000.0)
('Laptop', 40000.0)
('Keyboard', 500.0)
('Mouse', 400.0)
After Updating
('None', 30000.0)
('None', 40000.0)
('Keyboard', 500.0)
('Mouse', 400.0)

'''




