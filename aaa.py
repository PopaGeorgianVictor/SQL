import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='popa1993',
    port='3306',
    database='northwind'
)

mycursor = mydb.cursor()

mycursor.execute(" SELECT LastName, FirstName FROM Employees WHERE LastName BETWEEN 'J' AND 'M'")

query1  = mycursor.fetchall()
for q1 in query1:
    print(q1)





