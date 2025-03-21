import mysql.connector

dBase = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    passwd = 'password123',


)

# prepare a cursor object
cursorObject = dBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")

