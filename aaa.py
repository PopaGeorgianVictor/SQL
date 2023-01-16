import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='popa1993',
    port='3306',
    database='northwind'
)

mycursor = mydb.cursor()

mycursor.execute("select OrderDate, ShippedDate, CustomerID, Freight from Orders where OrderDate = '1997-05-19'")

query1  = mycursor.fetchall()
for q1 in query1:
    print(q1)





