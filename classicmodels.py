import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='popa1993',
    port='3306',
    database='classicmodels'
)

mycursor = mydb.cursor()


'''Check table presence in database schema'''

mycursor.execute('show tables')

query = mycursor.fetchall()
for q in query:
    print(q)


    
'''Check number of columns in a table'''

mycursor.execute('SELECT count(*) AS NumbersOfColumns FROM information_schema.columns WHERE table_name = "customers" ')

query = mycursor.fetchall()
for q in query:
    print(q)



    '''Check  column names in a table'''

mycursor.execute('SELECT column_name FROM information_schema.columns where table_name = "customers"')

query = mycursor.fetchall()
for q in query:
    print(q)



    '''Check  data type of columns  in  table'''

mycursor.execute('SELECT column_name,data_type FROM information_schema.columns where table_name = "customers"')

query = mycursor.fetchall()
for q in query:
    print(q)


    '''Check  size of columns  in  table'''

mycursor.execute('SELECT column_name,column_type FROM information_schema.columns where table_name = "customers"')

query = mycursor.fetchall()
for q in query:
    print(q)


    '''Check  nulls fields  in  table'''

mycursor.execute('SELECT column_name,is_nullable FROM information_schema.columns where table_name = "customers"')

query = mycursor.fetchall()
for q in query:
    print(q)

    
    '''Check  column keys  in  table'''

mycursor.execute('SELECT column_name,column_key FROM information_schema.columns where table_name = "customers"')

query = mycursor.fetchall()
for q in query:
    print(q)


    #Stored Procedure


# mycursor.execute('delimiter //'
                 
#                 'create procedure SelectAllCustomers()'
#                  'Begin'
#                     'select * from customers;'
#                  'End //'

#                  'delimiter ;')




# mycursor.execute('call SelectAllCustomers()')

# query = mycursor.fetchall()
# for q in query:
#     print(q)

# mycursor.execute('delimiter //'
                 
#                 'create procedure SelectAllCustomersByCity(IN mycity varchar(50))'
#                  'Begin'
#                     'select * from customers where city=mycity;'
#                  'End //'

#                  'delimiter ;')

# mycursor.execute('delimiter //'
                 
#                 'create procedure SelectAllCustomersByCityAndPin(IN mycity varchar(50), IN pcode varchar(15))'
#                  'Begin'
#                     'select * from customers where city=mycity and postalCode=pcode;'
#                  'End //'

#                  'delimiter ;')

# delimiter //

# CREATE PROCEDURE get_order_by_cust(
# IN cust_no INT,
# OUT shipped INT, OUT canceled INT,
# OUT resolved INT,
# OUT disputed INT)
# BEGIN
# -- shipped
# SELECT count(*) INTO shipped FROM orders WHERE customerNumber = cust_no AND status = 'Shipped';
# -- canceled
# SELECT count(*) INTO canceled FROM orders WHERE customerNumber = cust_no AND status = 'Canceled';
# -- resolved
# SELECT count(*) INTO resolved FROM orders WHERE customerNumber = cust_no AND status = 'Resolved';
# -- disputed
# SELECT count(*) INTO disputed FROM orders WHERE customerNumber = cust_no AND status = 'Disputed';

# End //
# delimiter ;

# CREATE PROCEDURE GetCustomerShipping(
# 	IN pCustomerNumber INT,
# 	OUT PShipping VARCHAR (50)
# )
# BEGIN
#     DECLARE customerCountry VARCHAR(100);
    
# SELECT country INTO customerCountry FROM customers WHERE customerNumber = pCustomerNumber;
# 	CASE customerCountry
# 		WHEN 'USA' THEN
# 			SET PShipping = '2-day Shipping';
# 		WHEN 'Canada' THEN
# 			SET PShipping = '3-day Shipping';
# 		ELSE
# 			SET PShipping = '5-day Shipping'; 
# END CASE;
# END //

# call GetCustomerShipping(112,@shipping)
# select @shhiping

# delimiter //

# CREATE PROCEDURE InsertSupplierProduct(IN inSupplierId INT, IN inProductId INT)
# BEGIN
# 	-- exit if the duplicate key occurs
# 	DECLARE EXIT HANDLER FOR 1062 SELECT 'Duplicate keys error encountered' Message; 
# 	DECLARE EXIT HANDLER FOR SQLEXCEPTION SELECT 'SQLException encountered' Message; 
# 	DECLARE EXIT HANDLER FOR SQLSTATE '23000' SELECT 'SQLSTATE 23000' ErrorCode;
    
# 	-- insert a new row into the Supplier Products
# 	INSERT INTO SupplierProducts(supplierId, productId) VALUES (inSupplierId, inProductId);
# 	-- return the products supplied by the supplier id
# 	SELECT COUNT(*) FROM SupplierProducts WHERE supplierId = inSupplierId;
# END //

# delimiter ;