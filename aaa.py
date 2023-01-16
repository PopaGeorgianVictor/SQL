import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='popa1993',
    port='3306',
    database='northwind'
)

mycursor = mydb.cursor()

mycursor.execute("select City, CompanyName, ContactName from Customers where City like ('A%') or City like ('B%')")

query1  = mycursor.fetchall()
for q1 in query1:
    print(q1)





