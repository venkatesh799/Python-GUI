import sqlite3  #importing 
conn=sqlite3.connect("database.db") #creating databse
c=conn.cursor()  #eastablishing connection with database
conn.commit()  #saving All Changes
conn.close()   #Closing Connection
