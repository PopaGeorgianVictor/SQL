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

# query = mycursor.fetchall()
# for q in query:
#     print(q)


mycursor.execute('call SelectAllCustomers()')

query = mycursor.fetchall()
for q in query:
    print(q)