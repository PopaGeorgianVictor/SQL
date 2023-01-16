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

'''RETURN THE TITLE OF COURTESY AND THE FIRST AND LAST NAME OF ALL EMPLOYEES 
WHOSE TITLE OF COURTESY BEGINS WITH "M" AND IS FOLLOWED BY ANY CHARACTER AND A PERIOD (.)'''

mycursor.execute("SELECT TitleOfCourtesy, FirstName, LastName FROM Employees "
                 "WHERE TitleOfCourtesy LIKE 'M%'")

query21 = mycursor.fetchall()
for q21 in query21:
    print(q21)

'''RETURN THE TITLE OF COURTESY AND THE FIRST AND LAST NAME OF ALL EMPLOYEES WHOSE TITLE OF COURTESY BEGINS WITH "M" 
AND IS FOLLOWED BY ANY CHARACTER AND A PERIOD (.)'''

mycursor.execute("SELECT TitleOfCourtesy, FirstName, LastName FROM Employees "
                 "WHERE TitleOfCourtesy LIKE 'M_.'")

query22 = mycursor.fetchall()
for q22 in query22:
    print(q22)

'''RETURN THE TITLE OF COURTESY AND THE FIRST AND LAST NAME OF ALL EMPLOYEES WHOSE TITLE OF COURTESY IS NOT "MS." OR "MRS.“'''

mycursor.execute("SELECT TitleOfCourtesy, FirstName, LastName FROM Employees "
                 "WHERE TitleOfCourtesy NOT In ('Ms.', 'Mrs.') ")

query23 = mycursor.fetchall()
for q23 in query23:
    print(q23)

'''RETURN THE FIRST AND LAST NAMES AND BIRTH DATE OF ALL EMPLOYEES BORN IN THE 1950S'''

mycursor.execute("SELECT firstname, lastname, birthdate FROM employees "
                 "WHERE birthdate BETWEEN '19500101' AND '19591231'  ")

query24 = mycursor.fetchall()
for q24 in query24:
    print(q24)

'''RETURN THE PRODUCT NAME AND SUPPLIER ID FOR ALL PRODUCTS SUPPLIED BY EXOTIC LIQUIDS, GRANDMA KELLY'S HOMESTEAD, AND TOKYO TRADERS. 
HINT: YOU WILL NEED TO FIRST DO A SEPARATE SELECT ON THE SUPPLIERS TABLE TO FIND THE SUPPLIER IDS OF THESE THREE COMPANIES.'''

mycursor.execute("SELECT ProductName, SupplierID FROM Products "
                 "WHERE SupplierID in (1, 3, 4 )")

query25 = mycursor.fetchall()
for q25 in query25:
    print(q25)

'''RETURN THE SHIPPING POSTAL CODE, ORDER ID, AND ORDER DATE FOR ALL ORDERS WITH A SHIP POSTAL CODE BEGINNING WITH "02389"'''

mycursor.execute("SELECT ShipPostalCode, OrderID, OrderDate FROM Orders "
                 "WHERE ShipPostalCode >= '02389'")

query26 = mycursor.fetchall()
for q26 in query26:
    print(q26)

'''RETURN THE CONTACT NAME AND TITLE AND THE COMPANY NAME FOR ALL CUSTOMERS WHOSE CONTACT TITLE DOES NOT CONTAIN THE WORD "SALES".'''

'''RETURN THE FIRST AND LAST NAME OF ALL SALES REPRESENTATIVES WHOSE TITLE OF COURTESY IS "MR."'''

'''RETURN THE FIRST AND LAST NAME AND THE CITY OF ALL EMPLOYEES WHO ARE FROM SEATTLE OR REDMOND'''

'''RETURN THE FIRST AND LAST NAME OF ALL SALES REPRESENTATIVES WHO ARE FROM SEATTLE OR REDMOND'''

'''RETURN THE FIRST AND LAST NAMES AND CITIES OF EMPLOYEES FROM CITIES OTHER THAN SEATTLE IN THE STATE OF WASHINGTON'''

'''RETURN THE COMPANY NAME, CONTACT TITLE, CITY AND COUNTRY OF ALL CUSTOMERS IN MEXICO OR IN ANY CITY IN SPAIN EXCEPT MADRID.
RETURN THE FULL NAME OF ALL EMPLOYEES'''

'''IF THE COST OF FREIGHT IS GREATER THAN OR EQUAL TO $500.00, IT WILL NOW BE TAXED BY 10%. RETURN THE ORDER ID, FREIGHT COST, FREIGHT COST WITH THIS TAX FOR ALL ORDERS OF $500 OR MORE.'''

'''Return all the orders and products ordered by all customers in April 1998. Return the
order ID, date of order, the product name, the customer first name and last name and quantity ordered for each product'''

'''Return the biggest list price of the products sold after 1998-04-01 (including this date).'''

'''Return for each customer return the number of orders in March 1998 and those orders total Freight value'''

'''Return which products were not ordered'''

'''Return the number of products from each category'''

'''Return the order ids and the associated employee names for orders that were shipped after the required date'''

'''Return the total quantity of products ordered. Only show records for products for which the quantity ordered is fewer than 200'''

'''Return the total number of orders by Customer since December 31, 1996. Return rows for which the number of orders is greater than 15'''

'''Return the company name, order id, and total price of all products of more than $10,000 worth'''

'''Return the Order ID, the name of the company that placed the order, and the first and last name of the associated employee.
Only show orders placed after January 1, 1998 that shipped after they were required. Sort by Company Name'''

'''Return the list of products that are beverages'''

'''Return the matching Customers and Suppliers by Country'''

'''Return the Customers that are from the same City and Country'''

'''Return the title and name of employees who have sold at least one of the products ‘Gravad Lax’ or ‘Mishi Kobe Niku’'''

'''Return the customer name, the product name and the supplier name for customers who live in London and whose suppliers
name is ‘Pavlova, Ltd.’ or ‘Karkki Oy’'''

'''Return all the orders and products ordered by all customers. Return the order date, the product name, the customer name and the supplier name'''

'''Return the biggest unit price of products sold to each customer'''

'''For each customer return the number of orders in the year 1996 and  those orders’ average product order size'''

'''Return all the customers who have placed orders'''

'''Return the number of orders and the orders total price for each customer'''

'''Return the number and the total of orders for each month of each year'''