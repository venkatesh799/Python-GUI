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
print("Before deleting")
for row in c.execute("select *from stocks"):
    print(row)

#Deleting Records
c.execute("delete from stocks where  price > 1000")

print("After deleting")

for row in c.execute("select *from stocks"):
    print(row)

conn.commit()  #saving All Changes

conn.close()   #Closing Connection


'''
OUTPUT

Before deleting
('Computer', 30000.0)
('Laptop', 40000.0)
('Keyboard', 500.0)
('Mouse', 400.0)
After deleting
('Keyboard', 500.0)
('Mouse', 400.0)

'''


