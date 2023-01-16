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

query1 = mycursor.fetchall()
for q1 in query1:
    print(q1)




'''RETURN THE PRODUCT NAME, QUANTITY PER UNIT AND UNIT PRICE FOR THE PRODUCTS THAT HAVE AT LEAST 10 UNITS IN STOCK 
AND THE UNIT PRICE IS LESS THAN 30 DOLARS ORDER BY PRODUCT NAME AND UNIT PRICE '''

mycursor.execute('SELECT ProductName, QuantityPerUnit, UnitPrice FROM Products '
                 'WHERE UnitsInStock = 10 AND UnitPrice < 30 '
                 'ORDER BY ProductName, UnitPrice ')

query2 = mycursor.fetchall()
for q2 in query2:
    print(q2)



'''RETURN THE NAME OF THE YOUNGEST EMPLOYEE'''

mycursor.execute('SELECT  LastName, FirstName FROM Employees '
                 'WHERE BirthDate = (SELECT MIN(BirthDate) AS EarliestDate FROM Employees)')

query3 = mycursor.fetchall()
for q3 in query3:
    print(q3)



'''RETURN THE FIRST NAME, LAST NAME, TITLE FOR THE SALES REPRESENTATIVE AND SALES MANAGERS EMPLOYEES'''

mycursor.execute("select FirstName, LastName, Title from Employees "
                 "where Title in ('sales representative', 'sales manager')")

query4 = mycursor.fetchall()
for q4 in query4:
    print(q4)



'''RETURN ALL EMPLOYEES THAT ARE NOT FROM LONDON, ORDER BY TITLE ASCENDING AND FIRST NAME DESCENDING'''

mycursor.execute("SELECT * FROM Employees "
                 "WHERE City <> 'London' ORDER BY Title, FirstName desc")

query5 = mycursor.fetchall()
for q5 in query5:
    print(q5)



'''RETURN ALL EMPLOYEES THAT DON’T HAVE THE REGION SET'''

mycursor.execute('SELECT * FROM Employees '
                 'WHERE Region is null')

query5 = mycursor.fetchall()
for q5 in query5:
    print(q5)



'''RETURN ALL PRODUCTS THAT HAVE THE NAME STARTING WITH “G”'''

mycursor.execute("SELECT * FROM Products "
                 "WHERE ProductName LIKE 'G%'")

query6 = mycursor.fetchall()
for q6 in query6:
    print(q6)



'''RETURN ALL PRODUCTS THAT HAVE THE NAME CONTAINING “AN” OR HAVE UNITS ON ORDER DIFFERENT FROM 0'''

mycursor.execute("SELECT * FROM Products "
                 "WHERE ProductName LIKE '%an%' OR UnitsOnOrder <> 0")

query7 = mycursor.fetchall()
for q7 in query7:
    print(q7)



'''RETURN ALL THE COMPANY NAMES AND CONTACT NAMES FOR WHICH THE CUSTOMERS ARE IN BUENOS AIRES'''

mycursor.execute("SELECT CompanyName, ContactName FROM Customers "
                 "WHERE City = 'Buenos Aires' ")

query8 = mycursor.fetchall()
for q8 in query8:
    print(q8)



'''RETURN THE ORDER DATE, SHIPPED DATE, CUSTOMER ID, AND FREIGHT OF ALL ORDERS PLACED ON MAY 19, 1997'''

mycursor.execute("SELECT OrderDate, ShippedDate, CustomerID, Freight FROM Orders "
                 "WHERE OrderDate = '1997-05-19' ")

query9 = mycursor.fetchall()
for q9 in query9:
    print(q9)



'''RETURN FIRST NAME, LAST NAME, AND COUNTRY OF ALL EMPLOYEES THAT ARE NOT IN THE UNITED STATES'''

mycursor.execute("SELECT FirstName, LastName, Country FROM Employees "
                 "WHERE Country <> 'USA'")

query10 = mycursor.fetchall()
for q10 in query10:
    print(q10)



'''RETURN THE EMPLOYEE ID, ORDER ID, CUSTOMER ID, SHIPPED DATE OF ALL ORDERS THAT WERE SHIPPED LATER THAN THEY WERE REQUIRED'''

mycursor.execute("SELECT EmployeeID, OrderID, CustomerID, ShippedDate "
                 "FROM Orders WHERE ShippedDate > RequiredDate")

query11 = mycursor.fetchall()
for q11 in query11:
    print(q11)



'''RETURN THE CITY, COMPANY NAME, AND CONTACT NAME OF ALL CUSTOMERS WHO ARE IN CITIES THAT BEGIN WITH "A" OR "B“'''

mycursor.execute("SELECT City, CompanyName, ContactName FROM Customers "
                 "WHERE City LIKE ('A%') or City LIKE ('B%')")

query12 = mycursor.fetchall()
for q12 in query12:
    print(q12)


''''''