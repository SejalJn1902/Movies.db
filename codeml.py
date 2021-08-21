import sqlite3
connection=sqlite3.connect('Movies.db')
cursor=connection.cursor()


command1=""" CREATE TABLE IF NOT EXISTS Movies(name TEXT PRIMARY KEY,actor TEXT,actress TEXT, director TEXT,year INTEGER) """

cursor.execute(command1)


cursor.execute(" INSERT INTO Movies VALUES ('Piku','Amitabh Bachchan','Deepika Padukone','Shoojit Sarkar',2015)")
cursor.execute(" INSERT INTO Movies VALUES ('Nayak','Anil Kapoor','Rani Mukharjee','S.Shankar',2001)")
cursor.execute(" INSERT INTO Movies VALUES ('Chennai Express','Sharukh Khan','Deepika Padukone','Rohit Shetty',2013)")
cursor.execute(" INSERT INTO Movies VALUES ('Dil Bechara','Sushant Singh Rajput','Sanjana Sanghi','Mukesh Chhabra',2020)")



cursor.execute("SELECT * FROM Movies")
results=cursor.fetchall()


cursor.execute("SELECT * FROM Movies WHERE actress='Deepika Padukone' ")
results2=cursor.fetchall()

#print the results
print(results)

print(results2)