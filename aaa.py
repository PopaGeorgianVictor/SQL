import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='popa1993',
    port='3306',
    database='northwind'
)

mycursor = mydb.cursor()
mycursor.execute(" SELECT FirstName, LastName, City from employees where City <> 'Seattle'  and  Country = 'USA'")

query30 = mycursor.fetchall()
for q30 in query30:
    print(q30)