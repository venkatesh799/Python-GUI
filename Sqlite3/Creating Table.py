import sqlite3  #importing 
conn=sqlite3.connect("database.db")  #creating databse
c=conn.cursor()  #eastablishing connection with database
c.execute('create table stocks(Item text,Price real)')  #creating table
conn.commit()  #saving All Changes
conn.close()   #Closing Connection


