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


'''RETURN ALL ORDERS THAT HAVE A FREIGHT COST OF MORE THAN $500.00'''

mycursor.execute("SELECT * FROM Orders "
                 "WHERE Freight > 500.00")

query13 = mycursor.fetchall()
for q13 in query13:
    print(q13)


'''RETURN THE PRODUCT NAME, UNITS IN STOCK, UNITS ON ORDER, AND REORDER LEVEL OF ALL PRODUCTS THAT ARE UP FOR REORDER'''

mycursor.execute("SELECT ProductName, UnitsInStock, UnitsOnOrder, ReorderLevel FROM Products "
                 "WHERE ReorderLevel > 0")

query14 = mycursor.fetchall()
for q14 in query14:
    print(q14)



'''RETURN THE COMPANY NAME, CONTACT NAME AND FAX NUMBER OF ALL CUSntactName,HAVE A FAX NUMBER'''

mycursor.execute("SELECT CompanyName, ContactName, Fax FROM Customers"
                 " WHERE Fax <> NULL")

query15 = mycursor.fetchall()
for q15 in query15:
    print(q15)



'''RETURN THE FIRST AND LAST NAME OF ALL EMPLOYEES WHO DO NOT REPORT TO ANYBODY'''

mycursor.execute("SELECT FirstName, LastName FROM Employees "
                 "WHERE ReportsTo is NULL")

query16 = mycursor.fetchall()
for q16 in query16:
    print(q16)


'''RETURN THE COMPANY NAME, CONTACT NAME AND FAX NUMBER OF ALL CUSTOMERS THAT HAVE A FAX NUMBER; SORT BY COMPANY NAME'''

mycursor.execute("SELECT CompanyName, ContactName , Fax FROM Customers "
                 "WHERE Fax is Not NULL Order by CompanyName")

query17 = mycursor.fetchall()
for q17 in query17:
    print(q17)



'''RETURN THE CITY, COMPANY NAME, AND CONTACT NAME OF ALL CUSTOMERS WHO ARE IN CITIES THAT BEGIN WITH "A" OR "B";
SORT BY CONTACT NAME DESCENDING'''

mycursor.execute("SELECT City, CompanyName, ContactName FROM Customers "
                 "WHERE City like ('A%') or City like ('B%') Order by ContactName DESC")

query18 = mycursor.fetchall()
for q18 in query18:
    print(q18)



'''RETURN THE FIRST AND LAST NAME OF ALL EMPLOYEES WHOSE LAST NAMES START WITH A LETTER BETWEEN "J" AND "M"'''

mycursor.execute("SELECT LastName, FirstName FROM Employees "
                 "WHERE LastName BETWEEN 'J' AND 'M'")

query19 = mycursor.fetchall()
for q19 in query19:
    print(q19)



'''CREATE A REPORT SHOWING THE TITLE OF COURTESY AND THE FIRST AND LAST NAME OF ALL EMPLOYEES WHOSE TITLE OF COURTESY IS "MRS." OR "MS."'''

mycursor.execute("SELECT TitleOfCourtesy, FirstName, LastName FROM Employees "
                 "WHERE TitleOfCourtesy IN ('Ms.', 'Mrs.')")

query20 = mycursor.fetchall()
for q20 in query20:
    print(q20)
