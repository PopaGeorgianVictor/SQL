import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='popa1993',
    port='3306',
    database='northwind'
)

mycursor = mydb.cursor()


mycursor.execute(" SELECT OrderID, Freight, Freight * 1.1 FROM Orders "
                 "WHERE Freight >= 500 ")

query30 = mycursor.fetchall()
for q30 in query30:
    print(q30)

