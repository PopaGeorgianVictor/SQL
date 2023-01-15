import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='popa1993',
    port='3306',
    database='northwind'
)

mycursor = mydb.cursor()



'''RETURN THE PRODUCT NAME, QUANTITY PER UNIT AND UNIT PRICE FOR ALL PRODUCTS ORDER BY PRODUCT NAME DESCENDING'''

mycursor.execute('SELECT ProductName, QuantityPerUnit, UnitPrice FROM Products '
                 'ORDER BY ProductName DESC ')

query1  = mycursor.fetchall()
for q1 in query1:
    print(q1)




'''RETURN THE PRODUCT NAME, QUANTITY PER UNIT AND UNIT PRICE FOR THE PRODUCTS THAT HAVE AT LEAST 10 UNITS IN STOCK 
AND THE UNIT PRICE IS LESS THAN 30 DOLARS ORDER BY PRODUCT NAME AND UNIT PRICE '''

mycursor.execute('SELECT ProductName, QuantityPerUnit, UnitPrice FROM Products '
                 'WHERE UnitsInStock = 10 AND UnitPrice < 30 '
                 'ORDER BY ProductName, UnitPrice ')

query2  = mycursor.fetchall()
for q2 in query2:
    print(q2)



'''RETURN THE NAME OF THE YOUNGEST EMPLOYEE'''

mycursor.execute('SELECT  LastName, FirstName FROM Employees '
                 'WHERE BirthDate = (SELECT MIN(BirthDate) AS EarliestDate FROM Employees)')

query3  = mycursor.fetchall()
for q3 in query3:
    print(q3)



'''RETURN THE FIRST NAME, LAST NAME, TITLE FOR THE SALES REPRESENTATIVE AND SALES MANAGERS EMPLOYEES'''

mycursor.execute("select FirstName, LastName, Title from Employees "
                 "where Title in ('sales representative', 'sales manager')")

query4  = mycursor.fetchall()
for q4 in query4:
    print(q4)


'''RETURN ALL EMPLOYEES THAT ARE NOT FROM LONDON, ORDER BY TITLE ASCENDING AND FIRST NAME DESCENDING'''

mycursor.execute("SELECT * FROM Employees "
                 "WHERE City <> 'London' ORDER BY Title, FirstName desc")

query5  = mycursor.fetchall()
for q5 in query5:
    print(q5)