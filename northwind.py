import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='popa1993',
    port='3306',
    database='northwind'
)

'''RETURN THE PRODUCT NAME, QUANTITY PER UNIT AND UNIT PRICE FOR ALL PRODUCTS ORDER BY PRODUCT NAME DESCENDING'''

mycursor = mydb.cursor()
mycursor.execute('SELECT ProductName, QuantityPerUnit, UnitPrice FROM Products '
                 'ORDER BY ProductName DESC ')

query1  = mycursor.fetchall()

for q1 in query1:
    print(q1)